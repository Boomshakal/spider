from celery.schedules import crontab

# 启动一个beat：celery beat -A celery_task -l info
# 启动work执行：celery worker -A celery_task -l info -P eventlet

broker_url = 'redis://:redis@192.168.234.129:6379/1'
result_backend = 'redis://:redis@192.168.234.129:6379/2'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = "Asia/Shanghai"  # 时区设置
worker_hijack_root_logger = False  # celery默认开启自己的日志，可关闭自定义日志，不关闭自定义日志输出为空
result_expires = 60 * 60 * 24  # 存储结果过期时间（默认1天）

# 导入任务所在文件
include = [
    "tasks1",  # 导入py文件
    "tasks2",
]

# 需要执行任务的配置
beat_schedule = {
    "test1": {
        "task": "tasks1.test_celery",  # 执行的函数
        "schedule": crontab(minute="*/1"),  # every minute 每分钟执行
        "args": ('定时执行1',)  # # 任务函数参数
    },

    "test2": {
        "task": "tasks2.test_celery2",
        "schedule": crontab(minute=0, hour="*/1"),  # every minute 每小时执行
        "args": ('定时执行2',)
    },

}
