from django.contrib import admin
from django.contrib.sites.models import Site
from .models import UserProfile, CardDetails
from django.contrib.auth.models import User

# Register your models here.
class CardDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'card_number',
        'exp_month',
        'exp_year',
        'cvc',
    )

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'car_registration',
        'card_details',
    )



admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CardDetails, CardDetailsAdmin)