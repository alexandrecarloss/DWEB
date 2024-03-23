from .models import Pet
from . import views as adocaoViews
from django.urls import path

urlpatterns = [
    path('<int: petid', adocaoViews.petdetalhe, name='petdetalhe'),
]