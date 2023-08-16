from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
User = settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
    pic = models.ImageField(upload_to='profile-pictures/', blank=True, null=True)
    



