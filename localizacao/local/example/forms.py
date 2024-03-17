from django import forms

from .models import Country, City

class LocationForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), 
        widget=forms.Select(attrs={"hx-get": "load_cities/", "hx-target": "#id_city"}))
    city = forms.ModelChoiceField(queryset=City.objects.none())