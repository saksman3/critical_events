from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField

# Create your models here.
class EventLog(models.Model):
    LogID = models.AutoField(auto_created=True,primary_key=True)
    event_id = models.IntegerField(max_length=100,unique=True)
    terminal_id = models.IntegerField(max_length=1000)
    vehicle_id = models.IntegerField(max_length=1000)
    vin = models.CharField(max_length=100)
    dealnumber = models.CharField(max_length=8)
    registration = models.CharField(max_length=100)
    vext = models.FloatField(blank=False)
    vgsm = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    gps_fix_type = models.IntegerField(max_length=2)
    ignition = models.IntegerField(max_length=2)
    event_ts = models.DateTimeField(blank=False)
    received_ts = models.DateTimeField(blank=False)
    created_ts = models.DateTimeField(blank=False)
    remote_addr = models.CharField(30)
    name = models.CharField(20,blank=True)
    sales_source_name = models.CharField(30,blank=True)
    vehicle_description = models.CharField(30,blank=True)
    year_of_manufacture = models.IntegerField(4,null=True)
    account_status = models.CharField(max_length=20,blank=True)
    arrears_amount = models.FloatField(max_length=30,null=True)
    exposure = models.CharField(30,default="")
    location_latitude = models.FloatField(max_length=5,default=0.00)
    location_longitude = models.FloatField(max_length=5,default=0.00)

class RequestResponse(models.Model):
    id = models.IntegerField(max_length=20,primary_key=True)
    response_ts = models.DateTimeField(blank=False, null=False)
    event_id = models.ForeignKey('EventLog',on_delete=CASCADE,)    #  check this field reference
    rating = models.IntegerField(max_length=10)
    vehicle_id = models.IntegerField(max_length=20)
    dealnumber = models.CharField(max_length=8)
