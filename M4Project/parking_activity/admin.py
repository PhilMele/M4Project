from django.contrib import admin
from .models import Stay, Fee
# Register your models here.

@admin.register(Stay)
class stay(admin.ModelAdmin):
    pass

@admin.register(Fee)
class free(admin.ModelAdmin):
    pass