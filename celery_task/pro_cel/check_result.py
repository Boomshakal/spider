from celery.result import AsyncResult
from celery_task.celery_app_task import app

async_task = AsyncResult(id="5a33b44d-10d0-4752-87ab-215a1644acbb", app=app)

if async_task.successful():
    result = async_task.get()
    print(result)
    # result.forget() # 将结果删除,执行完成，结果不会自动删除
    # async.revoke(terminate=True)  # 无论现在是什么时候，都要终止
    # async.revoke(terminate=False) # 如果任务还没有开始执行呢，那么就可以终止。
elif async_task.failed():
    print('执行失败')
elif async_task.status == 'PENDING':
    print('任务等待中被执行')
elif async_task.status == 'RETRY':
    print('任务异常后正在重试')
elif async_task.status == 'STARTED':
    print('任务已经开始被执行')
