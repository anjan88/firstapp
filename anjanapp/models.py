
# Create your models here.
from  __future__ import unicode_literals
from django.db import models

class Employee(models.Model):
    eno = models.CharField(max_length=264,unique=True)
    ename = models.CharField(max_length=264)
    email = models.EmailField(max_length=264, unique=True)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)