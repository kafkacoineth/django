# myapp/tasks.py
from celery import Celery, shared_task

celery_app = Celery('myapp')

@shared_task
def my_periodic_task():
    # Your task logic goes here
    print("Scheduled Task Executed")
    pass
