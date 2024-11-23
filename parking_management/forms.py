from django import forms
from django.forms import ModelForm
from .models import Parking, Rate, IllegalParking
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class ParkingForm(forms.ModelForm):
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
            'name':'',
            'max_capacity':'',
            'phone_number':'',
            'street_address1':'',
            'street_address2':'',
            'city':'',
            'county':'',
            'postcode':'',
            'country':'',
            'latitude':'',
            'longitude':'',
            'radius':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'aria-label': 'Parking Name', 'placeholder': 'Enter parking name'}),
            'max_capacity': forms.NumberInput(attrs={'aria-label': 'Maximum Capacity', 'placeholder': 'Parking Maximum Capacity'}),
            'phone_number': forms.TextInput(attrs={'aria-label': 'Phone Number', 'placeholder': 'Enter phone number'}),
            'street_address1': forms.TextInput(attrs={'aria-label': 'Street Address 1', 'placeholder': 'Enter street address 1'}),
            'street_address2': forms.TextInput(attrs={'aria-label': 'Street Address 2', 'placeholder': 'Enter street address 2'}),
            'city': forms.TextInput(attrs={'aria-label': 'City', 'placeholder': 'Enter city'}),
            'county': forms.TextInput(attrs={'aria-label': 'County', 'placeholder': 'Enter county'}),
            'postcode': forms.TextInput(attrs={'aria-label': 'Postcode', 'placeholder': 'Enter postcode'}),
            'country': CountrySelectWidget(attrs={'aria-label': 'Country', 'class': 'w-100'}),
            'latitude': forms.TextInput(attrs={'aria-label': 'Latitude', 'placeholder': 'Enter latitude'}),
            'longitude': forms.TextInput(attrs={'aria-label': 'Longitude', 'placeholder': 'Enter longitude'}),
            'radius': forms.TextInput(attrs={'aria-label': 'Radius', 'placeholder': 'Enter parking radius'}),
        }



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