from django.urls import path
from . import views

urlpatterns = [
    path('cadastropessoa/', views.cadastropessoa, name='accounts/cadastropessoa'),
]