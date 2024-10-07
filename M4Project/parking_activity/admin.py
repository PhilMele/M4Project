from django.contrib import admin
from .models import Stay, LeaveParking, EnterParking, UserPayment
# Register your models here.

class StayAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'parking_name',
        'calculated_fee'
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

class UserPaymentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'payment_bool',
        'stripe_checkout_id',
    )

admin.site.register(Stay, StayAdmin)

admin.site.register(EnterParking, EnterParkingAdmin)
admin.site.register(LeaveParking, LeaveParkingAdmin)
admin.site.register(UserPayment, UserPaymentAdmin)
