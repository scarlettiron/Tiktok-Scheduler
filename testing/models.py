from django.db import models

class test_model(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    schedule = models.DateTimeField()
    text = models.CharField(max_length=100, blank=True, null=True)
    uploaded = models.BooleanField(default=False)
