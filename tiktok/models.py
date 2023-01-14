from django.db import models

from django.conf import settings
User = settings.AUTH_USER_MODEL

class TiktokVideo(models.Model):
    file = models.FileField(upload_to='videos/tiktok/')
    date = models.DateTimeField(auto_now_add=True)
    uploaded = models.BooleanField(default=False)
    scheduled = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
