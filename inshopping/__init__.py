from __future__ import absolute_import, unicode_literals

# برای اطمینان از اینکه Celery در هنگام راه‌اندازی Django بارگذاری می‌شود
from .celery import app as celery_app

__all__ = ('celery_app',)
