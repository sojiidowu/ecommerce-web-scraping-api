import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_web_sraping.settings')

app = Celery('ecommerce_web_sraping')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()