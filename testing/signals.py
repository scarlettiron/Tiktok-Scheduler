from django.dispatch import receiver
from django.db.models import signals
from .models import test_model
from .tasks import test_process
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from celery.schedules import crontab
import json


def scheduled_test_process(objPk):
    schedule = CrontabSchedule.objects.create(
        hour = 5,
        minute = 2,
        day_of_month = 22,
        month_of_year = 1
    )
    

    task = PeriodicTask.objects.create(
        crontab = schedule, 
        name = f'upload-schedule-{objPk}',
        task = 'testing.tasks.test_process',
        one_off = True, 
        args = json.dumps([objPk]),
        enabled = True
        )
    print(task)

@receiver(signals.post_save, sender=test_model)
def create_scheduled_task(sender, instance, created, **kwargs):
    print(created)
    print(instance)
    if created:
        scheduled_test_process(instance.pk)
    return "done with step 1"
        

