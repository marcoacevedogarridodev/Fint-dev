from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
app = Celery('backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'fetch-mindicador-data-every-10-seconds': {
        'task': 'server.tasks.fetch_mindicador_data',
        'schedule': 10.0, 
    },
}
app.conf.timezone = 'UTC'
