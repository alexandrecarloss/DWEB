from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
import requests
from rest_framework.permissions import IsAuthenticated
from adocao.models import *
from .serializers import *
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

# ==================================== API V1 ====================================
class AvaliacoesAPIView(generics.ListCreateAPIView):
    """
        API de Avaliações
    """
    queryset = Avaliacao.objects.all().order_by('avacod')
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('pro_pk'):
            return self.queryset.filter(produto_proid = self.kwargs.get('pro_pk'))
        return self.queryset.all()

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Avaliação
    """
    queryset = Avaliacao.objects.all().order_by('avacod')
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('pro_pk'):
            return get_object_or_404(self.get_queryset(), produto_proid = self.kwargs.get('pro_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


class CarrinhosAPIView(generics.ListCreateAPIView):
    """
        API de Carrinhos
    """
    queryset = Carrinho.objects.all().order_by('carid')
    serializer_class = CarrinhoSerializer

class CarrinhoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Carrinho
    """
    queryset = Carrinho.objects.all().order_by('carid')
    serializer_class = CarrinhoSerializer


class FormaspagamentosAPIView(generics.ListCreateAPIView):
    """
        API de Formas de pagamentos
    """
    queryset = Formapagamento.objects.all().order_by('fpgid')
    serializer_class = FormapagamentoSerializer

class FormapagamentoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Forma de pagamento
    """
    queryset = Formapagamento.objects.all().order_by('fpgid')
    serializer_class = FormapagamentoSerializer


class ItensvendasAPIView(generics.ListCreateAPIView):
    """
        API de Itens vendas
    """
    queryset = Itemvenda.objects.all().order_by('itemvenda_venid')
    serializer_class = ItemvendaSerializer

class ItemvendaAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Item venda
    """
    queryset = Itemvenda.objects.all().order_by('itemvenda_venid')
    serializer_class = ItemvendaSerializer


class LoginsAPIView(generics.ListCreateAPIView):
    """
        API de Login
    """
    queryset = Login.objects.all().order_by('logemail')
    serializer_class = LoginSerializer

class LoginAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Login
    """
    queryset = Login.objects.all().order_by('logemail')
    serializer_class = LoginSerializer


class NotasfiscaisAPIView(generics.ListCreateAPIView):
    """
        API de Notas fiscais
    """
    queryset = Notafiscal.objects.all().order_by('ntfcod')
    serializer_class = NotafiscalSerializer

class NotafiscalAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Nota fiscal
    """
    queryset = Notafiscal.objects.all().order_by('ntfcod')
    serializer_class = NotafiscalSerializer


class OngsAPIView(generics.ListCreateAPIView):
    """
        API de Ongs
    """
    queryset = Ong.objects.all().order_by('ongid')
    serializer_class = OngSerializer

class OngAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Ong
    """
    queryset = Ong.objects.all().order_by('ongid')
    serializer_class = OngSerializer


class PessoasAPIView(generics.ListCreateAPIView):
    """
        API de Pessoas
    """
    queryset = Pessoa.objects.all().order_by('pesid')
    serializer_class = PessoaSerializer

class PessoaAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Pessoa
    """
    queryset = Pessoa.objects.all().order_by('pesid')
    serializer_class = PessoaSerializer


class PetsAPIView(generics.ListCreateAPIView):
    """
        API de Pets
    """
    queryset = Pet.objects.all().order_by('petid')
    serializer_class = PetSerializer

class PetAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Pet
    """
    queryset = Pet.objects.all().order_by('petid')
    serializer_class = PetSerializer


class PetsAdocoesAPIView(generics.ListCreateAPIView):
    """
        API de Pets Adoções
    """
    queryset = PetAdocao.objects.all().order_by('adoid')
    serializer_class = PetAdocaoSerializer

class PetAdocaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de PetAdocao
    """
    queryset = PetAdocao.objects.all().order_by('adoid')
    serializer_class = PetAdocaoSerializer


class PetsFotosAPIView(generics.ListCreateAPIView):
    """
        API de Pets Fotos
    """
    queryset = PetFoto.objects.all().order_by('pftid')
    serializer_class = PetFotoSerializer

class PetFotoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de PetFoto
    """
    queryset = PetFoto.objects.all().order_by('pftid')
    serializer_class = PetFotoSerializer


class PetsPortesAPIView(generics.ListCreateAPIView):
    """
        API de Pets Portes
    """
    queryset = PetPorte.objects.all().order_by('ptpid')
    serializer_class = PetPorteSerializer

class PetPorteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Pet Porte
    """
    queryset = PetPorte.objects.all().order_by('ptpid')
    serializer_class = PetPorteSerializer


class PetsRacasAPIView(generics.ListCreateAPIView):
    """
        API de Pets Racas
    """
    queryset = PetRaca.objects.all().order_by('ptrid')
    serializer_class = PetRacaSerializer

class PetRacaAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Pet Raca
    """
    queryset = PetRaca.objects.all().order_by('ptrid')
    serializer_class = PetRacaSerializer


class PetsTiposAPIView(generics.ListCreateAPIView):
    """
        API de Pets Tipos
    """
    queryset = PetTipo.objects.all().order_by('pttid')
    serializer_class = PetTipoSerializer

class PetTipoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Pet Tipo
    """
    queryset = PetTipo.objects.all().order_by('pttid')
    serializer_class = PetTipoSerializer


class PetshopsAPIView(generics.ListCreateAPIView):
    """
        API de Petshops
    """
    queryset = Petshop.objects.all().order_by('ptsid')
    serializer_class = PetshopSerializer

class PetshopAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Petshop
    """
    queryset = Petshop.objects.all().order_by('ptsid')
    serializer_class = PetshopSerializer


class ProdutosAPIView(generics.ListCreateAPIView):
    """
        API de produtos
    """
    queryset = Produto.objects.all().order_by('proid')
    serializer_class = ProdutoSerializer

class ProdutoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de produto
    """
    queryset = Produto.objects.all().order_by('proid')
    serializer_class = ProdutoSerializer


class ProdutosFotosAPIView(generics.ListCreateAPIView):
    """
        API de Produtos Fotos
    """
    queryset = ProdutoFoto.objects.all().order_by('prfid')
    serializer_class = ProdutoFotoSerializer

class ProdutoFotoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Produto Foto
    """
    queryset = ProdutoFoto.objects.all().order_by('prfid')
    serializer_class = ProdutoFotoSerializer
   

class ServicosAPIView(generics.ListCreateAPIView):
    """
        API de Serviços
    """
    queryset = Servico.objects.all().order_by('serid')
    serializer_class = ServicoSerializer

class ServicoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Servico
    """
    queryset = Servico.objects.all().order_by('serid')
    serializer_class = ServicoSerializer


class ServicosFotosAPIView(generics.ListCreateAPIView):
    """
        API de Serviços Fotos
    """
    queryset = ServicoFoto.objects.all().order_by('serftid')
    serializer_class = ServicoFotoSerializer

class ServicoFotoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Serviço Foto
    """
    queryset = ServicoFoto.objects.all().order_by('serftid')
    serializer_class = ServicoFotoSerializer


class SolicitacoesAPIView(generics.ListCreateAPIView):
    """
        API de Solicitações
    """
    queryset = Solicita.objects.all().order_by('solid')
    serializer_class = SolicitaSerializer

class SolicitaAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Solicita
    """
    queryset = Solicita.objects.all().order_by('solid')
    serializer_class = SolicitaSerializer


class TiposservicosAPIView(generics.ListCreateAPIView):
    """
        API de Tipos serviços
    """
    queryset = Tiposervico.objects.all().order_by('tpsid')
    serializer_class = TiposervicoSerializer

class TiposervicoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Tipo servico
    """
    queryset = Tiposervico.objects.all().order_by('tpsid')
    serializer_class = TiposervicoSerializer


class VendasAPIView(generics.ListCreateAPIView):
    """
        API de Vendas
    """
    queryset = Venda.objects.all().order_by('venid')
    serializer_class = VendaSerializer

class VendaAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        API de Venda
    """
    queryset = Venda.objects.all().order_by('venid')
    serializer_class = VendaSerializer
    

def prod(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/produtos/').json()
    return render(request, 'index.html', {'response': response})

# ==================================== API V2 ====================================

#   VIEWSET PADRÃO  
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all().order_by('avacod')
    serializer_class = AvaliacaoSerializer

#   VIEWSET CUSTOMIZADA
# class AvaliacaoViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
#     queryset = Avaliacao.objects.all().order_by('avacod')
#     serializer_class = AvaliacaoSerializer

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

class FormapagamentoViewSet(viewsets.ModelViewSet):
    queryset = Formapagamento.objects.all()
    serializer_class = FormapagamentoSerializer

class ItemvendaViewSet(viewsets.ModelViewSet):
    queryset = Itemvenda.objects.all()
    serializer_class = ItemvendaSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class NotafiscalViewSet(viewsets.ModelViewSet):
    queryset = Notafiscal.objects.all()
    serializer_class = NotafiscalSerializer

class OngViewSet(viewsets.ModelViewSet):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetAdocaoViewSet(viewsets.ModelViewSet):
    queryset = PetAdocao.objects.all()
    serializer_class = PetAdocaoSerializer
    
class PetFotoViewSet(viewsets.ModelViewSet):
    queryset = PetFoto.objects.all()
    serializer_class = PetFotoSerializer

class PetPorteViewSet(viewsets.ModelViewSet):
    queryset = PetPorte.objects.all()
    serializer_class = PetPorteSerializer

class PetRacaViewSet(viewsets.ModelViewSet):
    queryset = PetRaca.objects.all()
    serializer_class = PetRacaSerializer

class PetTipoViewSet(viewsets.ModelViewSet):
    queryset = PetTipo.objects.all()
    serializer_class = PetTipoSerializer

class PetshopViewSet(viewsets.ModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        
        #Pagination
        #self.pagination_class.page_size = 2
        avaliacoes = Avaliacao.objects.filter(produto_proid = pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many = True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes.all(), many=True)
        return Response(serializer.data)
    
class ProdutoFotoViewSet(viewsets.ModelViewSet):
    queryset = ProdutoFoto.objects.all()
    serializer_class = ProdutoFotoSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class ServicoFotoViewSet(viewsets.ModelViewSet):
    queryset = ServicoFoto.objects.all()
    serializer_class = ServicoFotoSerializer

class SolicitaViewSet(viewsets.ModelViewSet):
    queryset = Solicita.objects.all()
    serializer_class = SolicitaSerializer

class TiposervicoViewSet(viewsets.ModelViewSet):
    queryset = Tiposervico.objects.all()
    serializer_class = TiposervicoSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

