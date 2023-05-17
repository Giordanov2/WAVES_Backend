from django.db import models

# Create your models here.

class Vulnerability(models.Model):
    vulnerabilityId = models.CharField(max_length=70,blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    score = models.IntegerField(blank=False,default='')
    vulnerability_type = models.CharField(max_length=50,blank=False,default='')

class User(models.Model):
    username = models.CharField(max_length=70,blank=False, default='')
    name = models.CharField(max_length=70,blank=False, default='')
    lastname = models.CharField(max_length=70,blank=False, default='')
    email = models.EmailField(blank=False, default='')
    role = models.BooleanField(default=False)

class Technology(models.Model):
    tecnologyId = models.CharField(max_length=80, blank=False, default='')
    vendor = models.CharField(max_length=70, blank=False, default='')
    version = models.CharField(max_length=50, blank=False, default='')

class Scan(models.Model):
    target = models.CharField(max_length=80, blank=False, default='')