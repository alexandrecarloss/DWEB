from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('avaliacoes', AvaliacaoViewSet)
router.register('carrinhos', CarrinhoViewSet)
router.register('formaspagamentos', FormapagamentoViewSet)
router.register('itensvendas', ItemvendaViewSet)
router.register('logins', LoginViewSet)
router.register('notasfiscais', NotafiscalViewSet)
router.register('ongs', OngViewSet)
router.register('pessoas', PessoaViewSet)
router.register('pets', PetViewSet)
router.register('petsadocoes', PetAdocaoViewSet)
router.register('petsfotos', PetFotoViewSet)
router.register('petsportes', PetPorteViewSet)
router.register('petsracas', PetRacaViewSet)
router.register('petstipos', PetTipoViewSet)
router.register('petshops', PetshopViewSet)
router.register('produtos', ProdutoViewSet)
router.register('produtosfotos', ProdutoFotoViewSet)
router.register('servicos', ServicoViewSet)
router.register('servicosfotos', ServicoFotoViewSet)
router.register('solicitacoes', SolicitaViewSet)
router.register('tiposservicos', TiposervicoViewSet)
router.register('vendas', VendaViewSet)



urlpatterns = [
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='v1_avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='v1_avaliacao'),
    
    path('carrinhos/', CarrinhosAPIView.as_view(), name='v1_carrinhos'),
    path('carrinhos/<int:pk>/', CarrinhoAPIView.as_view(), name='v1_carrinho'),
    path('formaspagamentos/', FormaspagamentosAPIView.as_view(), name='v1_formaspagamentos'),
    path('formaspagamentos/<int:pk>/', FormapagamentoAPIView.as_view(), name='v1_formapagamento'),
    path('itensvendas/', ItensvendasAPIView.as_view(), name='v1_itensvendas'),
    path('itensvendas/<int:pk>/', ItemvendaAPIView.as_view(), name='v1_itemvenda'),
    path('logins/', LoginsAPIView.as_view(), name='v1_logins'),
    path('logins/<int:pk>/', LoginAPIView.as_view(), name='v1_login'),
    path('notasfiscais/', NotasfiscaisAPIView.as_view(), name='v1_notasfiscais'),
    path('notasfiscais/<int:pk>/', NotafiscalAPIView.as_view(), name='v1_notafiscal'),
    path('ongs/', OngsAPIView.as_view(), name='v1_ongs'),
    path('ongs/<int:pk>/', OngAPIView.as_view(), name='v1_ong'),
    path('pessoas/', PessoasAPIView.as_view(), name='v1_pessoas'),
    path('pessoas/<int:pk>/', PessoaAPIView.as_view(), name='v1_pessoa'),
    path('pets/', PetsAPIView.as_view(), name='v1_pets'),
    path('pets/<int:pk>/', PetAPIView.as_view(), name='v1_pet'),
    path('petsadocoes/', PetsAdocoesAPIView.as_view(), name='v1_petsadocoes'),
    path('petsadocoes/<int:pk>/', PetAdocaoAPIView.as_view(), name='v1_petadocao'),
    path('petsfotos/', PetsFotosAPIView.as_view(), name='v1_petsfotos'),
    path('petsfotos/<int:pk>/', PetFotoAPIView.as_view(), name='v1_petfoto'),
    path('petsportes/', PetsPortesAPIView.as_view(), name='v1_petsportes'),
    path('petsportes/<int:pk>/', PetPorteAPIView.as_view(), name='v1_petporte'),
    path('petsracas/', PetsRacasAPIView.as_view(), name='v1_petsracas'),
    path('petsracas/<int:pk>/', PetRacaAPIView.as_view(), name='v1_petraca'),
    path('petstipos/', PetsTiposAPIView.as_view(), name='v1_petstipos'),
    path('petstipos/<int:pk>/', PetTipoAPIView.as_view(), name='v1_pettipo'),
    path('petshops/', PetshopsAPIView.as_view(), name='v1_petshops'),
    path('petshops/<int:pk>/', PetshopAPIView.as_view(), name='v1_petshop'),

    path('produtos/', ProdutosAPIView.as_view(), name='v1_produtos'),
    path('produtos/<int:pk>/', ProdutoAPIView.as_view(), name='v1_produto'),
    path('produtos/<int:pro_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='v1_produto_avaliacoes'),
    path('produtos/<int:pro_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='produto_avaliacoes'),

    path('produtosfotos/', ProdutosFotosAPIView.as_view(), name='v1_produtosfotos'),
    path('produtosfotos/<int:pk>/', ProdutoFotoAPIView.as_view(), name='v1_produtofoto'),
    path('servicos/', ServicosAPIView.as_view(), name='v1_servicos'),
    path('servicos/<int:pk>/', ServicoAPIView.as_view(), name='v1_servico'),
    path('servicosfotos/', ServicosFotosAPIView.as_view(), name='v1_servicosfotos'),
    path('servicosfotos/<int:pk>/', ServicoFotoAPIView.as_view(), name='v1_servicofoto'),
    path('solicitacoes/', SolicitacoesAPIView.as_view(), name='v1_solicitacoes'),
    path('solicitacoes/<int:pk>/', SolicitaAPIView.as_view(), name='v1_solicita'),
    path('tiposservicos/', TiposservicosAPIView.as_view(), name='v1_tiposservicos'),
    path('tiposservicos/<int:pk>/', TiposervicoAPIView.as_view(), name='v1_tiposervico'),
    path('vendas/', VendasAPIView.as_view(), name='v1_vendas'),
    path('vendas/<int:pk>/', VendaAPIView.as_view(), name='v1_venda'),
    path('prod/', prod, name='prod'),
]