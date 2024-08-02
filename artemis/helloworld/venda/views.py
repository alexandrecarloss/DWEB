from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from adocao.views import *
from adocao.models import *
from udemydrf.views import *
import requests
from django.views.decorators.http import require_POST
from django.conf import settings
token = '8d5dec11c6d81e78b4aaa63bc56a98f53cf6f30e'
headers = {
    'Authorization': f'Token {token}',
    'Content-Type': 'application/json',
}

def produtos(request):
    # if request.method == 'POST':
    #     # URL da API
    #     url = 'http://127.0.0.1:8000/api/v1/produtos/'

    #     # Dados do produto
    #     produto = {
    #         "pronome": "Produto Exemplo",
    #         "propreco": 29.99,
    #         "prosaldo": 100,
    #         "propetshop_ptsid": 2,
    #         "prodtvalidade": "2024-12-31"
    #     }

    #     # Enviando a solicitação POST
    #     response = requests.post(url, json=produto)

    #     # Verificando a resposta
    #     if response.status_code == 201:
    #         print('Produto criado com sucesso!')
    #         print(response.json())
    #     else:
    #         print('Falha ao criar o produto:', response.status_code)
    #         print(response.json())

    # URL da API REST
    # api_url = 'http://127.0.0.1:8000/api/v1/produtos/'  # Altere para o URL real da sua API

    # # Fazendo a requisição GET para a API
    # response = requests.get(api_url)
    # if response.status_code == 200:
    #     produtos = response.json()  # Obtém os dados no formato JSON
    # else:
    #     produtos = []  # Em caso de erro, você pode definir um comportamento padrão
    # print(produtos)
    produtos = Produto.objects.all()
    # Renderiza o template passando os dados dos produtos
    return render(request, 'pagProdutos.html', {'produtos': produtos})

def produtosAntigo(request):
    # produtos = Produto.objects.all()
    # return render(request, 'produtos.html', {'produtos': produtos})
    produtos = Produto.objects.all()
    return render(request, 'pagProdutos.html', {'produtos': produtos})

def servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos.html', {'servicos': servicos})
# Create your views here.

####### CRUD produto
def insereservico(request):
    cursor = connection.cursor()
    petshop = Petshop.objects.filter(ptsemail=request.user.email).first()
    valor = request.POST.get('servalor')
    tipo = request.POST.get('servico')
    descricao = request.POST.get('serdescricao')
    try:
        cursor.execute('call sp_insere_servico (%(preco)s, %(petshop)s, %(tipo)s, %(descricao)s)', 
                {
                    'preco': valor, 
                    'petshop': petshop.ptsid, 
                    'tipo': tipo, 
                    'descricao': descricao, 
                })
        messages.success(request, 'Serviço adicionado com sucesso!')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao inserir Serviço!')
        return redirect(index)
    finally:
        cursor.close()
    return redirect(produtos)


def insereproduto(request):
    cursor = connection.cursor()
    pronome = request.POST.get('pronome')
    propreco = request.POST.get('propreco')
    prosaldo = request.POST.get('prosaldo')
    propetshop = request.POST.get('propetshop')
    provalidade = request.POST.get('provalidade')
    try:
        cursor.execute('call sp_insere_produto (%(nome)s, %(preco)s, %(saldo)s, %(petshop)s, %(validade)s)', 
                {
                    'nome': pronome, 
                    'preco': propreco, 
                    'saldo': prosaldo, 
                    'petshop': propetshop, 
                    'validade': provalidade, 
                })
        messages.success(request, 'Produto adicionado com sucesso!')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao inserir produto!')
        return redirect(index)
    finally:
        cursor.close()
    return redirect(produtos)

def alteraproduto(request, cod):
    cursor = connection.cursor()
    pronome = request.POST.get('pronome')
    propreco = request.POST.get('propreco')
    prosaldo = request.POST.get('prosaldo')
    propetshop = request.POST.get('propetshop')
    provalidade = request.POST.get('provalidade')
    try:
        cursor.execute('call sp_alteraproduto (%(nome)s, %(preco)s, %(saldo)s, %(petshop)s, %(validade)s, %(cod)s)', 
                {
                    'nome': pronome, 
                    'preco': propreco, 
                    'saldo': prosaldo, 
                    'petshop': propetshop, 
                    'validade': provalidade, 
                    'cod': cod
                })
        messages.success(request, 'Produto alterado com sucesso!')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao alterar produto!')
        return redirect(index)
    finally:
        cursor.close()
    return redirect(produtos)

def removerproduto(request, cod):
    produto = Produto.objects.filter(proid = cod).first()
    # Removendo fotos antigas
    try:
        prodfotos = ProdutoFoto.objects.filter(prfid = cod)
        for foto in prodfotos:
            foto.prffoto.delete()
            foto.delete()
        produto.delete()
        messages.success(request, 'Produto removido com sucesso!')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao remover produto!')
    return redirect(produtos)

###### CRUD serviço
def alteraservico(request, cod):
    cursor = connection.cursor()
    preco = request.POST.get('preco')
    petshop = request.POST.get('petshop')
    tipo = request.POST.get('tipo')
    decsricao = request.POST.get('decsricao')

    try:
        cursor.execute('call sp_alteraservico (%(preco)s, %(petshop)s, %(tipo)s, %(decsricao)s, %(cod)s)', {
                'preco': preco, 
                'petshop': petshop, 
                'tipo': tipo, 
                'decsricao': decsricao, 
                'cod': cod
            })
        messages.success(request, 'Serviço alterado com sucesso!')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao alterar serviço!')
        return redirect(index)
    finally:
        cursor.close()
    return redirect(servicos)

def removerservico(request, cod):
    # servico = Servico.objects.filter(serid = cod)
    # servico.delete()
    cursor = connection.cursor()
    try:
        cursor.execute('call sp_exclui_servico (%(cod)s', {
                'cod': cod
            })
        messages.success(request, 'Serviço removido com sucesso!')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao remover serviço!')
    return redirect(servicos)

@require_POST
@login_required(login_url="/accounts/login")
def post_produto(request):
    if str(request.user.groups.first()) == 'Pet shop':
        api_url = f"{settings.API_BASE_URL}/produtos/"
        pet_shop = Petshop.objects.filter(ptsemail = request.user.email).first()
        data = {
            "pronome": request.POST.get('pronome'),
            "propreco": request.POST.get('propreco'),
            "prosaldo": request.POST.get('prosaldo'),
            "propetshop_ptsid": pet_shop.ptsid,
            "prodtvalidade": request.POST.get('prodtvalidade'),    
        }
        response = requests.post(api_url, json=data, headers=headers)
        
        if response.status_code == 201:  # Created
            messages.success(request, 'Produto adicionado com sucesso!')
            return render(request, 'produtos.html')
        else:
            messages.error(request, 'Erro ao adicionar produto!')
            return render(request, 'produtos.html')
    else:
        messages.error(request, 'Somente petshops podem adicionar produto!')
        return render(request, 'produtos.html')
    
def adicionar_produto(request):
    tiposervicos =Tiposervico.objects.all()
    return render(request, 'produtos.html', {'tiposervicos': tiposervicos})

    
@login_required(login_url="/accounts/login")
def produto_detalhe(request, proid):
    if str(request.user.groups.first()) == 'Pessoa':
        pessoa = Pessoa.objects.filter(pesemail = str(request.user.email)).first()
        produto = Produto.objects.filter(proid = proid).first()
        return render(request, 'detalhes_produto.html', {'produto': produto, 'pessoa': pessoa})
    else:
        messages.error(request, 'Usuário deve ser uma pessoa física!')
        return render(request, 'index.html')

def carrinho_user(request, pesid):
    carrinhos = Carrinho.objects.filter(carpes = pesid)
    return render(request, 'pagina_carrinho.html', {'carrinhos': carrinhos})

@login_required(login_url="/accounts/login")
def inserir_produto_carrinho(request, proid):
    cursor = connection.cursor()
    produto = Produto.objects.filter(proid = request.POST.get('carpro')).first()
    carquant = request.POST.get('carquant')
    pessoa = Pessoa.objects.filter(pesemail = request.user.emaik).first()
    carpes = pessoa.pesid
    carpro = produto.proid
    if carquant <= produto.prosaldo:
        try:
            cursor.execute('call sp_insere_produto_carrinho (%(produto)s, %(pessoa)s, %(quantidade)s)', {'produto': carpro, 'pessoa': carpes, 'quantidade': carquant})
        except Exception as erro:
            print(erro)
            messages.error(request, 'Erro ao inserir produto ao carrinho!')
            return redirect(produtos)
        finally:
            cursor.close()
    else:
        messages.error(request, 'Quantidade de produto solicitada maior que o estoque!')
        return redirect(cadastropet)

    


