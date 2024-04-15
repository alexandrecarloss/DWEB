from django.urls import path
from . import views

urlpatterns = [
    path('', views.adocao, name='adocao'),
    path('load_racas/', views.load_racas, name="load_racas"),
    path('load_pets/', views.load_pets, name="load_pets"),
    path('petdetalhe/<int:petid>', views.petdetalhe, name="petdetalhe"),
    path('modalpet/<int:petid>', views.modalpet, name="modalpet"),
    path('cadastropet', views.cadastropet, name="cadastropet"),
    path('salvarpet', views.salvarpet, name="salvarpet"),
    path('atualizarpet/<int:petid>', views.atualizarpet, name="atualizarpet"),
    path('fotopet/<int:petid>/<int:multiplo>', views.fotopet.as_view(), name="fotopet"),
]