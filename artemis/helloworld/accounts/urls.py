from django.urls import path
from . import views

urlpatterns = [
    path('cadastropessoa/', views.cadastropessoa, name='accounts/cadastropessoa'),
    path('cadastro/', views.cadastro, name='accounts/cadastro'),
]