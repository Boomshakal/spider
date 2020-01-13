import celery

# broker='redis://127.0.0.1:6379/2' 不加密码
backend = 'redis://:redis@192.168.234.129:6379/1'
broker = 'redis://:redis@192.168.234.129:6379/2'
app = celery.Celery('test', backend=backend, broker=broker)


@app.task
def add(x, y):
    return x + y


app.conf.timezone = 'Asia/Shanghai'
app.conf.enable_utc = False
