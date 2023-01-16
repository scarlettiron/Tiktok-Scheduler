from django.urls import path
from . import views as v

urlpatterns = [
    #template version endpoint
    path('schedule-uplaod/', v.upload_tiktok, name='upload-tiktok-template'),
    #API version endpoint
    path('schedule-tiktok-upload/', v.ScheduleTiktokPost.as_view(), name='upload-tiktok-api'),
]
