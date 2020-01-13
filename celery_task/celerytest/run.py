from celery_app_task import app
if __name__ == '__main__':
    '''
    celery worker -A celery_app_task -l info -P eventlet
    '''
    app.worker_main()
    # cel.worker_main(argv=['--loglevel=info')