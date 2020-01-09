import pymysql,pymssql
from DBUtils.PooledDB import PooledDB
from database.settings import MYSQL,MSSQL


class MysqlPool:
    config = {
        'creator': pymysql,
        'host': MYSQL['HOST'],
        'port': MYSQL['PORT'],
        'user': MYSQL['USER'],
        'passwd': MYSQL['PASSWD'],
        'db': MYSQL['DB'],
        'charset': MYSQL['CHARSET'],
        'maxconnections': 70,  # 连接池最大连接数量
        'cursorclass': pymysql.cursors.DictCursor
    }
    pool = PooledDB(**config)

    def __enter__(self):
        self.conn = MysqlPool.pool.connection()
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()

    def db_conn(func):
        def wrapper(self, *args, **kw):
            with MysqlPool() as db:
                result = func(self, db, *args, **kw)
            return result

        return wrapper

    # 查询sql
    @db_conn
    def ExecQuery(self, db, sql, *args, **kw):
        db.cursor.execute(sql)
        relist = db.cursor.fetchall()
        return relist

    # 非查询的sql
    @db_conn
    def ExecNoQuery(self, db, sql):
        try:
            db.cursor.execute(sql)
            db.conn.commit()
            print("执行成功！")
        except Exception as e:
            db.conn.rollback()
            print(e)

class MssqlPool:
    config = {
        'creator': pymssql,
        'host': MSSQL['HOST'],
        # 'port': MSSQL['PORT'],
        'user': MSSQL['USER'],
        'password': MSSQL['PASSWD'],
        'database': MSSQL['DB'],
        'charset': MSSQL['CHARSET'],
        'maxconnections': 70,  # 连接池最大连接数量
        # 'cursorclass': pymssql.cursors.DictCursor
    }
    pool = PooledDB(**config)

    def __enter__(self):
        self.conn = MssqlPool.pool.connection()
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()

    def db_conn(func):
        def wrapper(self, *args, **kw):
            with MssqlPool() as db:
                result = func(self, db, *args, **kw)
            return result

        return wrapper

    # 查询sql
    @db_conn
    def ExecQuery(self, db, sql, *args, **kw):
        db.cursor.execute(sql)
        relist = db.cursor.fetchall()
        return relist

    # 非查询的sql
    @db_conn
    def ExecNoQuery(self, db, sql):
        try:
            db.cursor.execute(sql)
            db.conn.commit()
            print("执行成功！")
        except Exception as e:
            db.conn.rollback()
            print(e)

if __name__ == '__main__':

    connect = MysqlPool()

    lists = connect.ExecQuery('select * from goods_goods limit 3')

    for i in lists:
        print(i)
    #
    # connect.ExecNoQuery("update goods_goods set goods_sn='6666'  where id=52")

    # connect = MssqlPool()
    # lists = connect.ExecQuery('select top 5 * from mm_item')
    # for i in lists:
    #     print(i[0])

    # connect.ExecNoQuery('update mm_item set category_id=12  where id = 1')
