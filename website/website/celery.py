from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

app = Celery('website')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'my-periodic-task': {
        'task': 'store.tasks.my_periodic_task',
        'schedule': crontab(minute=0, hour='*'),  # Run once an hour at the start of the hour
    },
}

app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()
