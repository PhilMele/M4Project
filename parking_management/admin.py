from django.contrib import admin
from .models import Parking, Rate

# Register your models here.
class ParkingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'user',
        'bank_details'
    )

class RateAdmin(admin.ModelAdmin):
    list_display = (
    'rate_name',
    'user',
    'parking_name',
    'hour_range',
    'rate'
    )


admin.site.register(Parking, ParkingAdmin)
admin.site.register(Rate, RateAdmin)