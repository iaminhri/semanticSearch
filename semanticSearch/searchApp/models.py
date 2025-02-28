from django.db import models

# Create your models here.

class UserData(models.Model):
    name = models.CharField(max_length=255, blank=False)
    url = models.CharField(max_length=255, blank=False)
    source = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=255, blank=False)
    file = models.FileField(upload_to='media/', blank=False)