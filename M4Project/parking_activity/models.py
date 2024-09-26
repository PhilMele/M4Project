from django.db import models
from decimal import Decimal
from user_management.models import UserProfile
from parking_management.models import Parking

# Create your models here.
class Stay(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    timestamp_enter = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    timestamp_leave = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    parking_name = models.ForeignKey(Parking, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Fee (models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    calculated_fee = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    parking_name = models.ForeignKey(Parking, on_delete=models.CASCADE)

    def __str__(self):
        return f"Fee for {self.user} at {self.parking_name}: {self.calculated_fee}"