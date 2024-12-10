from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# logger module
import logging

# init logging
logger = logging.getLogger(__name__)

USER_TYPE = (
    (1, 'User'),
    (2, 'Parking Manager'),
)


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.IntegerField(choices=USER_TYPE, default=1)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)
    car_registration = models.CharField(max_length=80, null=True, blank=True)
    stripe_customer_id = models.CharField(
        max_length=250,
        null=True,
        blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        logger.info(f"Created new UserProfile for user {instance.username}.")
    else:
        # instead of creating a new user profile, update the existing one
        logger.info(
            f"User {instance.username} already exists, updating profile."
        )
    try:
        instance.userprofile.save()
    except UserProfile.DoesNotExist:
        logger.error(f"No UserProfile found for user {instance.username}.")
