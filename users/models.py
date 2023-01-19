from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
User = settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
    pic = models.ImageField(upload_to='profile-pictures/', blank=True, null=True)
    

platform_choices = [
    ('tiktok', 'Tiktok'),
]

class Social(models.Model):
    code = models.CharField(max_length=350)
    platform = models.CharField(choices = platform_choices, max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
