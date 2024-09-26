from django.contrib import admin
from .models import Parking

# Register your models here.
@admin.register(Parking)
class parking(admin.ModelAdmin):
    pass