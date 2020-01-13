# 222.py
from celery_task.celery import app

def test33():
    print("test33----------------")
    # print("------"*50)

def test44():
    print("test44--------------")
    # print("------" * 50)
    test33()

@app.task
def celery_run():
    test33()
    test44()


if __name__ == '__main__':
    celery_run()
