from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_account/', views.cadastro_account, name='cadastro_account'),
    # path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logoutaccount, name='logoutaccount'),
    path('login/', views.loginaccount, name='loginaccount'),
]