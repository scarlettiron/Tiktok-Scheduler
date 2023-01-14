from django.urls import path
from . import views as v

urlpatterns = [
    path('schedule-uplaod/', v.upload_tiktok, name='upload-tiktok-template'),
    
]
