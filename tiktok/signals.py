from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import TiktokVideo
from django_celery_beat.models import CrontabSchedule, PeriodicTask
import pendulum as pen
import json

@receiver(post_save, TiktokVideo)
def schedule_upload(self, instance, created, **kwargs):
    if not created or instance.uploaded == True:
        return 
    #time = pen.from_timestamp(instance.scheduled)
    time = pen.parse(instance.scheduled)
    print(time)
    crontab = CrontabSchedule.objects.create(
        minute = time.minute,
        hour = time.hour,
        day_of_month = time.day,
        month_of_year = time.month
    )
    task = PeriodicTask.objects.create(
        crontab = crontab,
        name = f"post upload {instance.pk}",
        task = 'tiktok.tasks.upload_post',
        enabled = True,
        one_off = True,
        args = json.dumps([instance.pk])
    )

