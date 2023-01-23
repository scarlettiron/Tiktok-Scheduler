from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class SupportedSocial(models.Model):
    name = models.CharField(max_length=100)
    auth_url = models.CharField(max_length=500)
    add_url = models.CharField(max_length=500) 
    token_url = models.CharField(max_length=500)

class Social(models.Model):
    code = models.CharField(max_length=350)
    platform = models.ForeignKey(SupportedSocial, on_delete=models.CASCADE, blank=True, null =True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


