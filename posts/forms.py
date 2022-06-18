from django import forms
from django.forms import ModelForm
from .models import Mountain

class MountainForm(ModelForm):
    class Meta:
        model = Mountain
        fields = ('name', 
        'latitude','longitude',
        'state','country','continent', 
        'elevation','google_maps_url',
        'glaciated',)
        labels = {
            'name': '',
            'latitude': '',
            'longitude': '',
            'state': '',
            'country': '',
            'continent': '',
            'elevation': '',
            'google_maps_url': '',
            'glaciated': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mountain/Peak Name'}),
            'latitude': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Latitude'}),
            'longitude': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Longitude'}),
            'state': forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),
            'country': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}),
            'continent': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Continent'}),
            'elevation': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Elevation (Feet)'}),
            'google_maps_url': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Google Maps Link'}),
            'glaciated': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Glaciated?'}),
        }
