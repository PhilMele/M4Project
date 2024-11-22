from django import forms
from django.forms import ModelForm
from .models import Parking, Rate, IllegalParking
from django_countries.fields import CountryField

class ParkingForm(ModelForm):

    name = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter parking name'})
    )
    max_capacity = forms.IntegerField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Parking Maximum Capacity'})
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
            'max_capacity',
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


class RateForm(ModelForm):

    rate_name = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter rate title'})
    )
    hour_range = forms.IntegerField(
        required=True, 
        label='', 
        widget=forms.NumberInput(attrs={'placeholder': 'Maximum hour until which rate is applicable'})
    )
    rate = forms.DecimalField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter applicable rate'})
    )
    class Meta:
        model = Rate
        fields = (
            'rate_name',
            'hour_range',
            'rate',
        )

class IllegalParkingForm(ModelForm):
    car_reg = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter reg.'})
    )
    class Meta:
        model = IllegalParking
        fields = (
            'car_reg',
        )