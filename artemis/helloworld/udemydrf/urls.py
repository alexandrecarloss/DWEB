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
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),

    path('carrinhos/', CarrinhosAPIView.as_view(), name='carrinhos'),
    path('carrinhos/<int:pk>/', CarrinhoAPIView.as_view(), name='carrinho'),
    path('formaspagamentos/', FormaspagamentosAPIView.as_view(), name='formaspagamentos'),
    path('formaspagamentos/<int:pk>/', FormapagamentoAPIView.as_view(), name='formapagamento'),
    path('itensvendas/', ItensvendasAPIView.as_view(), name='itensvendas'),
    path('itensvendas/<int:pk>/', ItemvendaAPIView.as_view(), name='itemvenda'),
    path('logins/', LoginsAPIView.as_view(), name='logins'),
    path('logins/<int:pk>/', LoginAPIView.as_view(), name='login'),
    path('notasfiscais/', NotasfiscaisAPIView.as_view(), name='notasfiscais'),
    path('notasfiscais/<int:pk>/', NotafiscalAPIView.as_view(), name='notafiscal'),
    path('ongs/', OngsAPIView.as_view(), name='ongs'),
    path('ongs/<int:pk>/', OngAPIView.as_view(), name='ong'),
    path('pessoas/', PessoasAPIView.as_view(), name='pessoas'),
    path('pessoas/<int:pk>/', PessoaAPIView.as_view(), name='pessoa'),
    path('pets/', PetsAPIView.as_view(), name='pets'),
    path('pets/<int:pk>/', PetAPIView.as_view(), name='pet'),
    path('petsadocoes/', PetsAdocoesAPIView.as_view(), name='petsadocoes'),
    path('petsadocoes/<int:pk>/', PetAdocaoAPIView.as_view(), name='petadocao'),
    path('petsfotos/', PetsFotosAPIView.as_view(), name='petsfotos'),
    path('petsfotos/<int:pk>/', PetFotoAPIView.as_view(), name='petfoto'),
    path('petsportes/', PetsPortesAPIView.as_view(), name='petsportes'),
    path('petsportes/<int:pk>/', PetPorteAPIView.as_view(), name='petporte'),
    path('petsracas/', PetsRacasAPIView.as_view(), name='petsracas'),
    path('petsracas/<int:pk>/', PetRacaAPIView.as_view(), name='petraca'),
    path('petstipos/', PetsTiposAPIView.as_view(), name='petstipos'),
    path('petstipos/<int:pk>/', PetTipoAPIView.as_view(), name='pettipo'),
    path('petshops/', PetshopsAPIView.as_view(), name='petshops'),
    path('petshops/<int:pk>/', PetshopAPIView.as_view(), name='petshop'),

    path('produtos/', ProdutosAPIView.as_view(), name='produtos'),
    path('produtos/<int:pk>/', ProdutoAPIView.as_view(), name='produto'),
    path('produtos/<int:pro_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='produto_avaliacoes'),
    path('produtos/<int:pro_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='produto_avaliacoes'),

    path('produtosfotos/', ProdutosFotosAPIView.as_view(), name='produtosfotos'),
    path('produtosfotos/<int:pk>/', ProdutoFotoAPIView.as_view(), name='produtofoto'),
    path('servicos/', ServicosAPIView.as_view(), name='servicos'),
    path('servicos/<int:pk>/', ServicoAPIView.as_view(), name='servico'),
    path('servicosfotos/', ServicosFotosAPIView.as_view(), name='servicosfotos'),
    path('servicosfotos/<int:pk>/', ServicoFotoAPIView.as_view(), name='servicofoto'),
    path('solicitacoes/', SolicitacoesAPIView.as_view(), name='solicitacoes'),
    path('solicitacoes/<int:pk>/', SolicitaAPIView.as_view(), name='solicita'),
    path('tiposservicos/', TiposservicosAPIView.as_view(), name='tiposservicos'),
    path('tiposservicos/<int:pk>/', TiposervicoAPIView.as_view(), name='tiposervico'),
    path('vendas/', VendasAPIView.as_view(), name='vendas'),
    path('vendas/<int:pk>/', VendaAPIView.as_view(), name='venda'),

    path('prod/', prod, name='prod'),
]