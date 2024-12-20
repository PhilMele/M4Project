from django import forms
from django.forms import ModelForm
from .models import Parking, Rate, IllegalParking
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator


class ParkingForm(forms.ModelForm):

    # restricts values in lat lng fields to didgits only
    latitude = forms.CharField(
        validators=[
            RegexValidator(
                # Allows latitude with up to 15 decimals
                regex=r'^([+-]?)((90(\.0{1,9})?)|([1-8]?[0-9])(\.\d{1,15})?)$',
                message=(
                    "Latitude must be a valid number (e.g., -90.0 to 90.0) "
                    "and up to 15 decimals."
                )
            )
        ],
        widget=forms.TextInput(
            attrs={'aria-label': 'Latitude', 'placeholder': 'Enter latitude'}),
        label=''
    )

    longitude = forms.CharField(
        validators=[
            RegexValidator(
                # Allows longitude with up to 15 decimals
                regex=(
                    r'^([+-]?)'
                    r'((180(\.0{1,9})?)|'
                    r'((1[0-7][0-9])|([1-9]?[0-9]))'
                    r'(\.\d{1,15})?)$'
                ),
                message=(
                    "Longitude must be a valid number (e.g., -180.0 to 180.0)"
                    " and up to 15 decimals.")
            )
        ],
        widget=forms.TextInput(
            attrs={
                'aria-label': 'Longitude',
                'placeholder': 'Enter longitude'
            }),
        label=''
    )

    radius = forms.IntegerField(
        validators=[
            MinValueValidator(
                50, message="Radius must be at least 50.")],
        widget=forms.NumberInput(
            attrs={
                'aria-label': 'Radius',
                'placeholder': 'Enter parking radius.'
            }),
        label=''
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
            'radius',
        )

        labels = {
            'name': '',
            'max_capacity': '',
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
            'name': forms.TextInput(
                attrs={
                    'aria-label': 'Parking Name',
                    'placeholder': 'Enter parking name'
                }),
            'max_capacity': forms.NumberInput(
                attrs={
                    'aria-label': 'Maximum Capacity',
                    'placeholder': 'Maximum Capacity'}),
            'phone_number': forms.TextInput(
                attrs={
                    'aria-label': 'Phone Number',
                    'placeholder': 'Enter phone number'}),
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
                    'class': 'w-100'}),
            'latitude': forms.TextInput(
                attrs={
                    'aria-label': 'Latitude',
                    'placeholder': 'Enter latitude'}),
            'longitude': forms.TextInput(
                attrs={
                    'aria-label': 'Longitude',
                    'placeholder': 'Enter longitude'}),
            'radius': forms.TextInput(
                attrs={
                    'aria-label': 'Radius',
                    'placeholder': 'Enter parking radius'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set all fields as required by default
        for field_name, field in self.fields.items():
            field.required = True

        # make  street_address2 not required
        self.fields['street_address2'].required = False


class RateForm(ModelForm):

    rate_name = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter rate title'})
    )
    hour_range = forms.IntegerField(
        required=True,
        label='',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Maximum hour until which rate is applicable'}),
        validators=[MinValueValidator(1)]
    )
    rate = forms.DecimalField(
        required=True,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter applicable rate'}),
        # prevents user to under values under or equal to 0
        validators=[MinValueValidator(0.01)]
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
