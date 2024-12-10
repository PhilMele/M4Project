from django import forms
from django.forms import ModelForm
from .models import UserProfile
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class UserProfileForm(ModelForm):
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

        labels = {
            'phone_number': '',
            'street_address1': '',
            'street_address2': '',
            'city': '',
            'county': '',
            'postcode': '',
            'country': '',
            'car_registration': '',
        }

        widgets = {
            'phone_number': forms.TextInput(
                attrs={
                    'aria-label': 'User Phone Number',
                    'placeholder': 'Enter Phone Number'}),
            'car_registration': forms.TextInput(
                attrs={
                    'aria-label': 'User Car Registration Name',
                    'placeholder': 'Enter Car registration'}),
            'street_address1': forms.TextInput(
                attrs={
                    'aria-label': 'Street Address 1',
                    'placeholder': 'Enter street address 1'}),
            'street_address2': forms.TextInput(
                attrs={
                    'aria-label': 'Street Address 2',
                    'placeholder': 'Enter street address 2'}),
            'city': forms.TextInput(
                attrs={
                    'aria-label': 'City',
                    'placeholder': 'Enter city'}),
            'county': forms.TextInput(
                attrs={
                    'aria-label': 'County',
                    'placeholder': 'Enter county'}),
            'postcode': forms.TextInput(
                attrs={
                    'aria-label': 'Postcode',
                    'placeholder': 'Enter postcode'}),
            'country': CountrySelectWidget(
                attrs={
                    'aria-label': 'Country',
                    'class': 'w-100'
                }),
        }
