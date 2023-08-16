from django.db import models
from SocialPlatforms.models import Social, SupportedSocial

from django.conf import settings
User = settings.AUTH_USER_MODEL

class TiktokVideo(models.Model):
    link = models.CharField(max_length=500, blank=True, null=True)
    file = models.FileField(upload_to='videos/tiktok/')
    date = models.DateTimeField(auto_now_add=True)
    uploaded = models.BooleanField(default=False)
    scheduled = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platforms = models.ManyToManyField(Social)
    errors = models.CharField(max_length=1000, blank=True, null = True)

