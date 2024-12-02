from django.contrib import admin
from django.contrib.sites.models import Site
from .models import UserProfile
from django.contrib.auth.models import User

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'car_registration',
    )



admin.site.register(UserProfile, UserProfileAdmin)