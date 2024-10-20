from django.db import models
from django_countries.fields import CountryField
from user_management.models import UserProfile
from decimal import Decimal

# Create your models here.
class Parking (models.Model):
    name = models.CharField(max_length=80)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)
    latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)
    longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
    radius = models.CharField(verbose_name="Radius",max_length=50, null=True, blank=True)
    bank_details = models.CharField(max_length=80, null=True, blank=True)


    def __str__(self):
        return self.name

class Rate (models.Model):
    rate_name = models.CharField(max_length=80)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    parking_name = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True, blank=True)
    hour_range = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    timestamp_leave = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.rate_name
