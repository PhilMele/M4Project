from django import forms
from django.forms import ModelForm
from .models import Parking
from django_countries.fields import CountryField

class ParkingForm(ModelForm):
    name = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter parking name'})
    )
    phone_number = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter phone number'})
    )
    street_address1 = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter street address 1'})
    )
    street_address2 = forms.CharField(
        required=False, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter street address 2'})
    )
    city = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter city'})
    )
    county = forms.CharField(
        required=False, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter county'})
    )
    postcode = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter postcode'})
    )
    country = CountryField()
    latitude = forms.DecimalField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter latitude'})
    )
    longitude = forms.DecimalField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter longitude'})
    )
    radius = forms.DecimalField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter parking radius'})
    )

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
            'radius'
        )