from django.urls import path
from . import views

urlpatterns = [
    path('insereproduto/', views.insereproduto, name="insereproduto"),
    path('produtosAntigo/', views.produtosAntigo, name="produtosAntigo"),
    path('produtos/', views.produtos, name="produtos"),
    path('alteraproduto/<int:cod>/', views.alteraproduto, name="alteraproduto"),
    path('removerproduto/<int:cod>/', views.removerproduto, name="removerproduto"),
    path('servicos/', views.servicos, name="servicos"),
    path('alteraservico/<int:cod>/', views.alteraservico, name="alteraservico"),
    path('removerservico/<int:cod>/', views.removerservico, name="removerservico"),
    path('post_produto/', views.post_produto, name="post_produto"),
    path('adicionar_produto/', views.adicionar_produto, name="adicionar_produto"),
    path('produto_detalhe/<int:proid>/', views.produto_detalhe, name="produto_detalhe"),
    path('carrinho_user/<int:pesid>/', views.carrinho_user, name="carrinho_user"),
    path('inserir_produto_carrinho/<int:proid>/', views.inserir_produto_carrinho, name="inserir_produto_carrinho"),
]