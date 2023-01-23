
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #for native template rendering version
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('tiktok/', include('tiktok.urls')), 
    path('users/', include('users.urls')),
    path('socials/', include('SocialPlatforms.urls')),
    path('test/', include('testing.urls')),
]
