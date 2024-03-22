from django import forms

from .models import PetTipo, PetRaca, Pet

# class especieForm(forms.Form):
#     especie = forms.ModelChoiceField(queryset = PetTipo.objects.all(),
#         widget=forms.Select(attrs={"hx-get": "load_racas/", "hx-target": "#id_raca"}))
#     raca = forms.ModelChoiceField(queryset = PetRaca.objects.none(), label='Raça')

class especieForm(forms.Form):
    especie = forms.ModelChoiceField(queryset = PetTipo.objects.all(),
        widget=forms.Select(attrs={"hx-get": "load_racas/", "hx-target": "#id_raca"}))
    raca = forms.ModelChoiceField(queryset = PetRaca.objects.none(), label='Raça',
        widget=forms.Select(attrs={"hx-get": "load_pets/", "hx-target": "#containercardspets"}))
    