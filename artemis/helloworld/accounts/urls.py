from django.urls import path
from . import views

urlpatterns = [
    path('cadastropessoa/', views.cadastropessoa, name='cadastropessoa'),
    # path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logoutaccount, name='logoutaccount'),
    path('login/', views.loginaccount, name='loginaccount'),
]