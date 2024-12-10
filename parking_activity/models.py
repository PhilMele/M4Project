from django.db import models
from decimal import Decimal
from user_management.models import UserProfile
from parking_management.models import Parking
from django.dispatch import receiver
from django.db.models.signals import post_save



# Create your models here.
class Stay(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    parking_name = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True, blank=True)
    calculated_fee = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    stripe_checkout_id = models.CharField(max_length=500, default="")
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"

#note: there is redundancy in some of the FK, but equally adds more visibility from admin panel
class EnterParking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    parking_name = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True, blank=True)
    stay = models.ForeignKey(Stay, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp_enter = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"

class LeaveParking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    parking_name = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True, blank=True)
    stay = models.ForeignKey(Stay, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp_leave = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"

#payment logic: credits: https://www.youtube.com/watch?v=hZYWtK2k1P8&t=1s


