from django.urls import path, include
from . import views
from adocao import views as viewsadocao

urlpatterns = [
    path('cadastro_dados/', views.cadastro_dados, name='cadastro_dados'),
    path('cadastro_email_enviado/', views.cadastro_email_enviado, name='cadastro_email_enviado'),
    path('logout/', views.logoutaccount, name='logoutaccount'),
    path('login/', views.loginaccount, name='loginaccount'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('accountsdjango/', include("django.contrib.auth.urls")),
    path('usuario/', views.usuario, name='usuario'),
    path('ong/', views.ong, name='ong'),
    path('atualizar_pessoa/<int:pesid>', views.atualizar_pessoa, name='atualizar_pessoa'),
    path('atualizar_ong/<int:ongid>', views.atualizar_ong, name='atualizar_ong'),
    path('cadastro_user/', views.cadastro_user, name='cadastro_user'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<str:uidb64>/<str:token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/complete/', views.reset_complete, name='reset_complete'),
    path('adicionarpet/', views.adicionarpet, name="adicionarpet"),
    path('petshop/', views.petshop, name='petshop'),
    
]