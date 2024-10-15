from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

class CardDetails(models.Model):
    card_number = models.CharField(max_length=80, null=True, blank=True)
    exp_month = models.CharField(max_length=2, null=True, blank=True)
    exp_year = models.CharField(max_length=4, null=True, blank=True)
    cvc = models.CharField(max_length=3, null=True, blank=True)


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
    card_details = models.ForeignKey(CardDetails, on_delete=models.SET_NULL, null=True, blank=True)
    car_registration = models.CharField(max_length=80, null=True, blank=True)
    stripe_customer_id = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        print(f"User {instance.username} has been created with ID {instance.id}.")
        UserProfile.objects.create(user=instance)
    else:
        #instead of creating a new userprofile
        #if the userprofile already exists its gets updated.
        print(f"User {instance.username} already exists, updating profile.")
    # If the userprofile doesn't exist yet, this will raise an exception
    try:
        instance.userprofile.save()
    except UserProfile.DoesNotExist:
        print("No UserProfile found for this user.")