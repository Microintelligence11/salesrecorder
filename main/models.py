from typing import ValuesView
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class saleData(models.Model):
    date = models.DateField(blank=True,null=True)
    cosName = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    serviceName = models.CharField(max_length=100)
    price = models.IntegerField()
    usr = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)


class expanceData(models.Model):
    date = models.DateField(blank=True,null=True)
    buyerName = models.CharField(max_length=100)
    buyerPhone = models.CharField(max_length=12)
    buyerEmail = models.EmailField()
    serviceName = models.CharField(max_length=100)
    price = models.IntegerField()
    usr = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)

class contact(models.Model):
    name = models.CharField(max_length=50,default="")
    phone = models.IntegerField(default="")
    email = models.EmailField(default="")  
    address = models.CharField(max_length=50,default="")
    quary = models.CharField(max_length=50,default='')
    usr = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)