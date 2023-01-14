from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pic = models.ImageField(upload_to='profile-pictures/', blank=True, null=True)
    
