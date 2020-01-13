from tasks1 import test_celery
from tasks2 import test_celery2

# 立即告知celery去执行test_celery任务，并传入一个参数
result = test_celery.delay('第一个的执行')
print(result.id)
result = test_celery2.delay('第二个的执行')
print(result.id)
