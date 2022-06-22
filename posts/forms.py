from django import forms
from django.forms import ModelForm
from .models import Mountain, ClimbEvent

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

#---Admin SuperUser Event Form---#
class ClimbEventForm(ModelForm):
    class Meta:
        model = ClimbEvent
        fields = ('mountain', 
        'event_date','user','attendees','description',)
        labels = {
            'mountain': 'Mountain',
            'event_date': 'YYYY-MM-DD',
            'user': 'Leader',
            'attendees': 'Climbers',
            'description':'',
        }
        widgets = {
            'mountain': forms.Select(attrs={'class':'form-control', 'placeholder':'Mountain/Peak Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-select', 'placeholder':'Event Date'}),
            'user': forms.Select(attrs={'class':'form-select', 'placeholder':'Leader'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
        }

#---User Event Form---#
# class ClimbEventForm(ModelForm):
#     class Meta:
#         model = ClimbEvent
#         fields = ('mountain', 
#         'event_date','user','attendees','description',)
#         labels = {
#             'mountain': 'Mountain',
#             'event_date': 'YYYY-MM-DD',
#             'user': 'Leader',
#             'attendees': 'Climbers',
#             'description':'',
#         }
#         widgets = {
#             'mountain': forms.Select(attrs={'class':'form-control', 'placeholder':'Mountain/Peak Name'}),
#             'event_date': forms.TextInput(attrs={'class':'form-select', 'placeholder':'Event Date'}),
#             'user': forms.Select(attrs={'class':'form-select', 'placeholder':'Leader'}),
#             'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
#             'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
#         }

