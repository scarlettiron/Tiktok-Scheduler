from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tiktok_scheduler.settings")
app = Celery("tiktok_scheduler")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.result_chord_join_timeout = 900
app.conf.result_chord_retry_interval = 5
app.conf.result_expires = timedelta(days=3)


