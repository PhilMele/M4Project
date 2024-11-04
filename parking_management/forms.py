from django import forms
from django.forms import ModelForm
from .models import Parking

class ParkingForm(ModelForm):
    class Meta:
        model = Parking
        fields = (
            'name',
            'phone_number',
            'street_address1',
            'street_address2',
            'city',
            'county',
            'postcode',
            'country',
            'latitude',
            'longitude',
            'radius')
        labels ={
            'name': '',
            'phone_number': '',
            'street_address1': '',
            'street_address2': '',
            'city': '',
            'county': '',
            'postcode': '',
            'country': '',
            'latitude': '',
            'longitude': '',
            'radius': '',
        }
        widgets = {  
                }
