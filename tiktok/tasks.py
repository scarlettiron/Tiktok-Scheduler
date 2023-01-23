from tiktok_scheduler.celery import app
from celery import shared_task
from django.db.models import OuterRef

from .models import TiktokVideo
from SocialPlatforms.models import Social
from SocialPlatforms.platform_auth import TiktokUtils

#when new tasks are created you must use taskname.delay()
#to make sure user is not having to wait on task

@shared_task(bind=True)
def upload_post(self, objPk):
    objPk = int(objPk)
    post = TiktokVideo.objects.filter(pk=objPk).select_related('user').prefetch_related(
                                        'platforms', queryset= Social.objects.filter(
                                        user__pk = OuterRef('user__pk')).select_related(
                                        'platform'), to_attr = 'platforms')[0]
    print(post)
    for platform in post.platforms:
        print(platform)
        try:
            if platform.platform.name == 'tiktok':
                TiktokUtils.upload_post()
        except:
            pass
    

