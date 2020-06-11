from tasks1 import test_celery
from tasks2 import test_celery2

# 立即告知celery去执行test_celery任务，并传入一个参数
result = test_celery.delay('第一个的执行')
print(result.id)
result = test_celery2.delay('第二个的执行')
print(result.id)

tp = time.time()
utc_time = datetime.datetime.utcfromtimestamp(tp)
add_time = datetime.timedelta(seconds=10)
utc_time = utc_time + add_time
result = test_celery.apply_async(args=('定时任务'), eta=utc_time)
