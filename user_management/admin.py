from django.contrib import admin
from django.contrib.sites.models import Site
from .models import UserProfile
from django.contrib.auth.models import User

# Register your models here.

@admin.register(UserProfile)
class userprofile(admin.ModelAdmin):
    pass