# 111.py
from celery_task.celery import app

def test11():
    print("test11----------------")

def test22():
    print("test22--------------")
    test11()

@app.task
def celery_run():
    test11()
    test22()

if __name__ == '__main__':
    celery_run()
