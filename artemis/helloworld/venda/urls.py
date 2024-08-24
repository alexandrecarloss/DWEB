from django.urls import path
from . import views

urlpatterns = [
    #Crud produto
    path('insereproduto/', views.insereproduto, name="insereproduto"),
    path('produtos/', views.produtos, name="produtos"),
    path('alteraproduto/<int:proid>/', views.alteraproduto, name="alteraproduto"),
    path('removerproduto/<int:cod>/', views.removerproduto, name="removerproduto"),
    path('adicionar_produto/', views.adicionar_produto, name="adicionar_produto"),
    path('produto_detalhe/<int:proid>/', views.produto_detalhe, name="produto_detalhe"),
    path('petshop_produto_detalhe/<int:proid>/', views.petshop_produto_detalhe, name="petshop_produto_detalhe"),
    path('fotoproduto/<int:proid>/<int:multiplo>/', views.fotoproduto.as_view(), name="fotoproduto"),
    path('load_produtos_categoria/', views.load_produtos_categoria, name="load_produtos_categoria"),
    path('form_altera_produto/<int:proid>/', views.form_altera_produto, name='form_altera_produto'),
    #Crud serviço
    path('servicos/', views.servicos, name="servicos"),
    path('alteraservico/<int:serid>/', views.alteraservico, name="alteraservico"),
    path('removerservico/<int:cod>/', views.removerservico, name="removerservico"),
    path('insereservico/', views.insereservico, name="insereservico"),
    path('form_altera_servico/<int:serid>/', views.form_altera_servico, name='form_altera_servico'),
    #Carrinho
    path('carrinho_user/', views.carrinho_user, name="carrinho_user"),
    path('inserir_produto_carrinho/<int:proid>/', views.inserir_produto_carrinho, name="inserir_produto_carrinho"),
    path('remover_produto_carrinho/<int:carid>/', views.remover_produto_carrinho, name="remover_produto_carrinho"),
    path('checkout_produto/', views.checkout_produto, name="checkout_produto"),
    path('finaliza_compra/', views.finaliza_compra, name="finaliza_compra"),
    #Agendamento
    path('load_servicos_local/<int:petid>/<int:tpsid>/', views.load_servicos_local, name='load_servicos_local'),
    path('agendar_servico_pet/', views.agendar_servico_pet, name="agendar_servico_pet"),
    path('agendar_servico_servico/', views.agendar_servico_servico, name="agendar_servico_servico"),
    path('agendar_servico_local/<int:petid>/', views.agendar_servico_local, name="agendar_servico_local"),
    path('agendar_servico_data/<int:petid>/<int:tpsid>/', views.agendar_servico_data, name='agendar_servico_data'),
    path('agendar_servico_servico_voltar/<int:petid>/', views.agendar_servico_servico_voltar, name="agendar_servico_servico_voltar"),
    path('agendar_servico_local_voltar/<int:petid>/<int:tpsid>/', views.agendar_servico_local_voltar, name='agendar_servico_local_voltar'),
    #Solicita
    path('solicita_servico/<int:petid>/<int:serid>/', views.solicita_servico, name='solicita_servico'),
    path('cancelar_solicitacao/<int:solid>/', views.cancelar_solicitacao, name='cancelar_solicitacao'),
    path('solicitar_servico_junto', views.solicitar_servico_junto, name='solicitar_servico_junto'),
    path('select_cidades_tpservico/', views.select_cidades_tpservico, name="select_cidades_tpservico"),
    path('load_petshop_cidade/', views.load_petshop_cidade, name='load_petshop_cidade'),
    path('solicita_servico_junto', views.solicita_servico_junto, name='solicita_servico_junto'),
    path('usuario_produto_detalhe/<int:proid>/', views.usuario_produto_detalhe, name="usuario_produto_detalhe"),
    #Mudar estado de solicitação de serviço 
    path('aceitar_solicitacao/<int:solid>/', views.aceitar_solicitacao, name="aceitar_solicitacao"),
    path('negar_solicitacao/<int:solid>/', views.negar_solicitacao, name="negar_solicitacao"),  
    #Crud avaliação
    path('insere_avaliacao_produto/<int:proid>/', views.insere_avaliacao_produto, name="insere_avaliacao_produto"),
    path('insere_avaliacao_servico/<int:serid>/', views.insere_avaliacao_servico, name="insere_avaliacao_servico"), 
    path('exclui_avaliacao/<int:avacod>/', views.exclui_avaliacao, name="exclui_avaliacao"),  
    path('altera_avaliacao/<int:avacod>/', views.altera_avaliacao, name="altera_avaliacao"), 
    #Dashboard para pet shop
    path('petshop_relatorio_faturamento_venda/', views.petshop_relatorio_faturamento_venda, name='petshop_relatorio_faturamento_venda'),
    path('petshop_relatorio_produto_categoria/', views.petshop_relatorio_produto_categoria, name='petshop_relatorio_produto_categoria'),
    path('petshop_relatorio_quantidade_venda/', views.petshop_relatorio_quantidade_venda, name='petshop_relatorio_quantidade_venda'),
    #Retorno de valor int
    path('retorna_receita_mes/', views.retorna_receita_mes, name='retorna_receita_mes'),
    
    
    #Dashboard para pessoa
    path('usuario_relatorio_gastos_produtos/', views.usuario_relatorio_gastos_produtos, name='usuario_relatorio_gastos_produtos'),
    path('usuario_relatorio_gastos_servicos/', views.usuario_relatorio_gastos_servicos, name='usuario_relatorio_gastos_servicos'),
    path('usuario_relatorio_produto_categoria/', views.usuario_relatorio_produto_categoria, name='usuario_relatorio_produto_categoria'),
    path('usuario_relatorio_produto_categoria_gastos/', views.usuario_relatorio_produto_categoria_gastos, name='usuario_relatorio_produto_categoria_gastos'),
    
    
    
]