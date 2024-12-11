from django import forms
from django.forms import ModelForm
from .models import Stay


class StayForm(ModelForm):
    class Meta:
        model = Stay
        fields = ('parking_name',)
        labels = {
            'parking_name': '',

        }
        widgets = {
                    'parking_name': forms.Select(
                        attrs={'class': 'form-control'}),
                }
