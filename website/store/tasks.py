# myapp/tasks.py

from celery import shared_task

@shared_task
def my_periodic_task():
    # Your task logic goes here
    print("Scheduled Task Executed")
    pass
