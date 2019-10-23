# from django.db import models

# Create your models here.
from djongo import models
from djongo.models import forms

class HotelDetails(models.Model):
    options_available = [('yes','yes'),('no','no')]
    hotel_name = models.CharField( max_length=255)
    hotel_id = models.IntegerField(max_digits=6)
    store_name = models.CharField( max_length=255, unique=True)
    location =models.CharField(max_length = 2000, blank= True)
    owner_name = models.CharField( max_length=255)
    email_id = models.EmailField(max_digits=15)
    contact_number = models.IntegerField(max_digits=10)
    oyo_amount = models.IntegerField(max_digits=15)
    options = models.CharField( max_length=3, choices=options_available)
    comments = models.CharField( max_length=250)

    latitude = models.IntegerField(max_digits=6)
    longitude = models.DecimalField(max_digits=6, decimal_places=3)
