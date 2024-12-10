from django.db import models
from django_countries.fields import CountryField
from user_management.models import UserProfile
from decimal import Decimal
from django.core.exceptions import ValidationError


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
    country = CountryField(default='GB')
    max_capacity = models.IntegerField(default='50')
    latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)
    longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
    radius = models.CharField(verbose_name="Radius",max_length=50, null=True, blank=True, default='50')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Rate (models.Model):
    rate_name = models.CharField(max_length=80)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    parking_name = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True, blank=True)
    hour_range = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    timestamp_leave = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def clean(self):
        # rate validator: checks if rate field value is not already assigned to another 
        # rate object with same parkind_id
        # this is to avoid parking manager creating different rates for the same hour range
        if Rate.objects.filter(parking_name=self.parking_name, hour_range=self.hour_range).exclude(id=self.id).exclude(parking_name__isnull=True).exists():
            raise ValidationError("An hour range with this value already exists for the selected parking.")

    def __str__(self):
        return self.rate_name

class IllegalParking(models.Model):
    inspector = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    parking_name = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True, blank=True)
    car_reg = models.CharField(max_length=80)

    def __str__(self):
        return self.parking_name

    def __str__(self):
            # Return a string representation that handles potential None values
            parking_name_str = self.parking_name.name if self.parking_name else "Unknown Parking"
            return f"{parking_name_str} - {self.car_reg}"