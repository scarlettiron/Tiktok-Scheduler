from tiktok_scheduler.celery import app
from .models import test_model
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from celery import shared_task
from django.http import HttpResponse

#@app.task(bind=True)
@shared_task(bind=True)
def test_process(self, objPk):
    print('starting proces')
    objPk = int(objPk)
    test = test_model.objects.get(pk=objPk)
    test.text = 'it worked'
    test.uploaded = True
    test.save()
    return "done with testing task"

    

