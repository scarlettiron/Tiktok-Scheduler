from django.urls import path
from . import views as v


urlpatterns = [
    path('add-platform/', v.add_social_template, name='add-platform-template'),
    path('add-platform-redirect/', v.add_social_return_uri, name='add-platform-return-uri'),
]
