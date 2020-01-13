import time
from celery_app_task import app


@app.task
def test_celery2(res):
    time.sleep(5)
    return "test_celery2任务结果:%s" % res
