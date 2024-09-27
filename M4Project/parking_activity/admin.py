from django.contrib import admin
from .models import Stay, Fee, LeaveParking, EnterParking
# Register your models here.

class StayAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'parking_name'
    )

class LeaveParkingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'parking_name',
        'stay',
        'timestamp_leave',
    )

class FeeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'calculated_fee',
        'parking_name',
    )

class EnterParkingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'parking_name',
        'stay',
        'timestamp_enter',
    )

admin.site.register(Stay, StayAdmin)
admin.site.register(Fee, FeeAdmin)
admin.site.register(EnterParking, EnterParkingAdmin)
admin.site.register(LeaveParking, LeaveParkingAdmin)
