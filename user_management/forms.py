from django import forms
from django.forms import ModelForm
from .models import UserProfile

class UserProfileForm(ModelForm):
    phone_number = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter phone number'})
    )

    street_address1 = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter first line of address'})
    )

    street_address2 = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter second line of address'})
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

    country = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter country'})
    )

    car_registration = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Enter car registration'})
    )

    class Meta:
        model = UserProfile
        fields = (
          name',
            'phone_number',
            'street_address1',
            'street_address2',
            'city', 
            'county',
            'postcode',
            'country',
            'car_registration',
        )