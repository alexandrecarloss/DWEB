from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.produtos, name="produtos"),
]