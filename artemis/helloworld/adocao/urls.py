from django.urls import path
from . import views

urlpatterns = [
    path('', views.adocao, name='adocao'),
    path('load_racas/', views.load_racas, name="load_racas"),
    path('load_pets/', views.load_pets, name="load_pets"),
    path('petdetalhe/<int:petid>/', views.petdetalhe, name="petdetalhe"),
    path('modalpet/<int:petid>/', views.modalpet, name="modalpet"),
    path('cadastropet/', views.cadastropet, name="cadastropet"),
    path('salvarpet/', views.salvarpet, name="salvarpet"),
    path('atualizarpet/<int:petid>/', views.atualizarpet, name="atualizarpet"),
    path('removerpet/<int:petid>/', views.removerpet, name="removerpet"),
    path('fotopet/<int:petid>/<int:multiplo>/', views.fotopet.as_view(), name="fotopet"),
    path('inicia_adocao/<int:pesid>/<int:adoid>/', views.inicia_adocao, name="inicia_adocao"),
    path('altera_status_adocao_aceito/<int:ttaid>/', views.altera_status_adocao_aceito, name='altera_status_adocao_aceito'),
    path('altera_status_adocao_negado/<int:ttaid>/', views.altera_status_adocao_negado, name='altera_status_adocao_negado'),
    path('altera_status_adocao_adotado/<int:ttaid>/', views.altera_status_adocao_adotado, name='altera_status_adocao_adotado'),
    path('altera_status_adocao_nao_adotado/<int:ttaid>/', views.altera_status_adocao_nao_adotado, name='altera_status_adocao_nao_adotado'),
    #Dashboard para ong
    path('ong_relatorio_adocoes_concluidas/', views.ong_relatorio_adocoes_concluidas, name='ong_relatorio_adocoes_concluidas'),
    path('ong_relatorio_adocoes_concluidas_tipo/', views.ong_relatorio_adocoes_concluidas_tipo, name='ong_relatorio_adocoes_concluidas_tipo'),

    #Retorno de Valores
    path('retorna_total_adocoes/', views.retorna_total_adocoes, name='retorna_total_adocoes'),
    
]