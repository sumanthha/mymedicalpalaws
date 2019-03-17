from __future__ import unicode_literals

from django.db import models

# Create your models here.
'''
class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address   = models.CharField(max_length=300)
    address2  = models.CharField(max_length=300)
    address3  = models.CharField(max_length=300)
    city      = models.CharField(max_length=100)
    state     = models.CharField(max_length=100)
    country   = models.CharField(max_length=200)
    phone     = models.CharField(max_length=100)
    email     = models.CharField(max_length=100)

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=30)
    address     = models.CharField(max_length=300)
    address2    = models.CharField(max_length=300)
    city        = models.CharField(max_length=100)
    state       = models.CharField(max_length=100)
    country     = models.CharField(max_length=200)
    phone       = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Report(models.Model):
    report_type = models.CharField(max_length=200)
    report_s3_location = models.CharField(max_length=500)

'''