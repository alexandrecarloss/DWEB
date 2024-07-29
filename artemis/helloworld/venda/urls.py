from django.urls import path
from . import views

urlpatterns = [
    path('insereproduto/', views.insereproduto, name="insereproduto"),
    path('produtos/', views.produtos, name="produtos"),
    path('alteraproduto/<int:cod>/', views.alteraproduto, name="alteraproduto"),
    path('removerproduto/<int:cod>/', views.removerproduto, name="removerproduto"),
    path('servicos/', views.servicos, name="servicos"),
    path('alteraservico/<int:cod>/', views.alteraservico, name="alteraservico"),
    path('removerservico/<int:cod>/', views.removerservico, name="removerservico"),
]