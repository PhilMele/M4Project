from django.contrib import admin
from .models import Stay, Fee, LeaveParking, EnterParking
# Register your models here.

@admin.register(Stay)
class stay(admin.ModelAdmin):
    pass

@admin.register(Fee)
class fee(admin.ModelAdmin):
    pass

@admin.register(EnterParking)
class enterparking(admin.ModelAdmin):
    pass

@admin.register(LeaveParking)
class leaveparking(admin.ModelAdmin):
    pass