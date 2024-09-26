from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)
    bank_details = models.CharField(max_length=80, null=True, blank=True)
    car_registration = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username
        
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create the UserProfile when a new User is created
        UserProfile.objects.create(user=instance)
    else:
        # Ensure the UserProfile exists + save it
        try:
            instance.userprofile.save()
        except UserProfile.DoesNotExist:
            # If the user profile doesn't exist then create it
            UserProfile.objects.create(user=instance)