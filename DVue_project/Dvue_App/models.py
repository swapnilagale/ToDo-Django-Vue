from pydoc import describe
from django.db import models

class Task(models.Model):
    STATUS_CHOICES=(
        ('todo','TODO'),
        ('done','DONE')
    )

    description=models.CharField(max_length=255)

    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='todo')