import pymysql, pymssql
from DBUtils.PooledDB import PooledDB
from settings import MYSQL, MSSQL

import sentry_sdk

# sentry报错收集服务器
sentry_sdk.init("https://89f2e30912c64c1c8b4da5b739e706a8@sentry.io/1876964")


# 装饰器用于使用with开关调用__enter__ 和 __exit__
def db_conn(func):
    def wrapper(self, *args, **kw):
        with self as db:
            result = func(self, db, *args, **kw)
        return result

    return wrapper


# mssql 结果转换dict
def get_dict(row_list, col_list):
    cols = [d[0] for d in col_list]
    res_list = []
    for row in row_list:
        res_list.append(dict(zip(cols, row)))  # 将两个列表合并成一个字典 dict(zip())方法
    return res_list


class DatabasePool(object):
    def __init__(self, db):
        self.type = db
        if self.type == "mysql":
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
        else:
            config = {
                'creator': pymssql,
                'host': MSSQL['HOST'],
                # 'port': MSSQL['PORT'],
                'user': MSSQL['USER'],
                'password': MSSQL['PASSWD'],
                'database': MSSQL['DB'],
                'charset': MSSQL['CHARSET'],
                'maxconnections': 70,  # 连接池最大连接数量
                # 'cursorclass': pymysql.cursors.DictCursor
            }
        self.pool = PooledDB(**config)

    def __enter__(self):
        self.conn = self.pool.connection()
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()

    # 查询sql
    @db_conn
    def ExecQuery(self, db, sql, *args, **kw):
        db.cursor.execute(sql)
        relist = db.cursor.fetchall()
        if self.type == 'mysql':
            return relist
        else:
            desc_res = db.cursor.description
            return get_dict(relist, desc_res)

    # 非查询的sql
    @db_conn
    def ExecNoQuery(self, db, sql, *args, **kw):
        try:
            db.cursor.execute(sql)
            db.conn.commit()
            print("执行成功！")
        except Exception as e:
            db.conn.rollback()
            print(e)


if __name__ == '__main__':
    # connect = DatabasePool('mysql')
    #
    # lists = connect.ExecQuery('select * from goods_goods limit 3')
    #
    # for i in lists:
    #     print(i)
    #
    # connect.ExecNoQuery("update goods_goods set goods_sn='6666'  where id=52")

    #########
    ##mssql##
    #########
    sql = '''
    exec p_mm_wo_workshop_plan_get_items_finereport
    
    '''
    connect = DatabasePool('mssql')
    lists = connect.ExecQuery(sql)

    for i in lists:
        print(i)

    # connect.ExecNoQuery('update mm_item set category_id=12  where id = 1')
