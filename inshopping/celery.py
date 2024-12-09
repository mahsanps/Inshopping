from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# تنظیمات محیطی Django برای Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inshopping.settings')

app = Celery('inshopping')

# از تنظیمات Django برای Celery استفاده می‌کنیم
app.config_from_object('django.conf:settings', namespace='CELERY')

# وظایف را از فایل‌ها پیدا می‌کنیم
app.autodiscover_tasks()
