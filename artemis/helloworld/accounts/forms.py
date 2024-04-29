from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Uma conta com esse endereço de email já existe!")
        return email
    
class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})