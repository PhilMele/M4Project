from django import forms
from django.forms import ModelForm
from .models import UserProfile
from django_countries.fields import CountryField

class UserProfileForm(ModelForm):
    phone_number = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter phone number'})
    )

    street_address1 = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter 1st line of address'})
    )

    street_address2 = forms.CharField(
        required=False, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter 2nd line of address'})
    )

    city = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter city'})
    )

    county = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter county'})
    )

    postcode = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter postcode'})
    )

    country = CountryField()

    car_registration = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter car registration'})
    )

    class Meta:
        model = UserProfile
        fields = (
            'phone_number',
            'street_address1',
            'street_address2',
            'city', 
            'county',
            'postcode',
            'country',
            'car_registration',
        )