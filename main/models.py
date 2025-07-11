from django.db import models
from datetime import  datetime
# Create your models here.

class Blog(models.Model):
    image = models.CharField(max_length=100000,default="",blank=True)
    header = models.CharField(max_length=100)
    text = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now,blank=True)