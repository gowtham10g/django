from django.db import models
import datetime
from django.utils import timezone

class intern(models.Model):
    name = models.CharField(max_length=100,unique=True,default='default_name')
    pdf = models.FileField(upload_to ="intern/pdf",blank=False,default='default_name')
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=("-date_created",)