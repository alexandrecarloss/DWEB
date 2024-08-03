from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from adocao.views import *
from adocao.models import *
from udemydrf.views import *
from accounts.views import *
import requests
from django.views.decorators.http import require_POST
from django.conf import settings
token = '8d5dec11c6d81e78b4aaa63bc56a98f53cf6f30e'
headers = {
    'Authorization': f'Token {token}',
    'Content-Type': 'application/json',
}

def produtos(request):
    nome_produto_pesquisa = request.GET.get('nome_produto_pesquisa')
    if nome_produto_pesquisa:
         produtos_todos = Produto.objects.all().filter(pronome__icontains = nome_produto_pesquisa)
    else:
        produtos_todos = Produto.objects.all()
    produtos = []
    for p in produtos_todos:
        if p.prosaldo > 0:
            produtos.append(p)
    return render(request, 'pagProdutos.html', {'produtos': produtos})

def servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos.html', {'servicos': servicos})
# Create your views here.

##################### CRUD produto #####################
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
    categoriaproduto = request.POST.get('categoriaproduto')
    v_petshop = Petshop.objects.filter(ptsemail = request.user.email).first()
    propetshop = v_petshop.ptsid
    try:
        cursor.execute('call sp_insere_produto (%(nome)s, %(preco)s, %(saldo)s, %(petshop)s, %(categoria)s)', 
        {
            'nome': pronome, 
            'preco': propreco, 
            'saldo': prosaldo, 
            'petshop': propetshop,
            'categoria': categoriaproduto
        })
        # produto_novo = Produto.objects.order_by('-ptsid')[0]
        produto_novo = Produto.objects.order_by('-proid')[0]
        print('produto novo', produto_novo)
        profotos_novo = request.FILES.getlist("profoto")
        if profotos_novo:
            for foto in profotos_novo:
                produto_foto_novo = ProdutoFoto(prffoto = foto, produto_proid = produto_novo)
                produto_foto_novo.save()
        messages.success(request, 'Produto adicionado com sucesso!')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao inserir produto!')
        return redirect(index)
    finally:
        cursor.close()
    return redirect(petshop)

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
    
def adicionar_produto(request):
    contexto = context_grupo_usuario(request)
    if contexto['dado_usuario'] == None:
        messages.error(request, 'Termine seu cadastro')
        return redirect(cadastro_dados)
    tiposervicos =Tiposervico.objects.all()
    categorias = CategoriaProduto.objects.all()
    return render(request, 'cadastro_prod_serv.html', {'tiposervicos': tiposervicos, 'categorias': categorias})

    
@login_required(login_url="/accounts/login")
def produto_detalhe(request, proid):
    if str(request.user.groups.first()) == 'Pessoa':
        pessoa = Pessoa.objects.filter(pesemail = str(request.user.email)).first()
        produto = Produto.objects.filter(proid = proid).first()
        fotos_produto = ProdutoFoto.objects.filter(produto_proid = produto.proid)
        return render(request, 'detalhes_produto.html', {'produto': produto, 'pessoa': pessoa, 'fotos_produto': fotos_produto})
    else:
        messages.error(request, 'Usuário deve ser uma pessoa física!')
        return render(request, 'index.html')

@login_required(login_url="/accounts/login")
def carrinho_user(request):
    if str(request.user.groups.all()[0]) == 'Pessoa':
        pessoa = Pessoa.objects.filter(pesemail = request.user.email).first()
        pesid = pessoa.pesid
        carrinhos = Carrinho.objects.filter(carpes = pesid)
        total_carrinhos = 0
        for c in carrinhos:
            total_carrinhos = total_carrinhos + c.carpreco
        return render(request, 'pagina_carrinho.html', {'carrinhos': carrinhos, 'total_carrinhos': total_carrinhos})
    else:
        messages.error(request, 'Usuário deve ser uma pessoa física!')
        return render(request, 'index.html')

@login_required(login_url="/accounts/login")
def inserir_produto_carrinho(request, proid):
    cursor = connection.cursor()
    produto = Produto.objects.filter(proid = proid).first()
    carquant = int(request.POST.get('carquant'))
    pessoa = Pessoa.objects.filter(pesemail = request.user.email).first()
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
            if carquant == 1:
                messages.success(request, f'{carquant} {produto.pronome} adicionado ao carrinho com sucesso!')
            else:
                messages.success(request, f'{carquant} {produto.pronome} adicionados ao carrinho com sucesso!')
                produto.prosaldo = produto.prosaldo - carquant
                produto.save()
            return redirect(carrinho_user)
    else:
        messages.error(request, 'Quantidade de produto solicitada maior que o estoque!')
        return redirect(produtos)

@login_required(login_url="/accounts/login")
def remover_produto_carrinho(request, carid):
    carrinho = Carrinho.objects.filter(carid = carid).first()
    try:
        #Devolvendo o saldo de produto
        produto = Produto.objects.filter(proid = carrinho.carpro.proid).first()
        produto.prosaldo = produto.prosaldo + carrinho.carquant
        produto.save()
        carrinho.delete()
        messages.success(request, f'{produto.pronome} removido do carrinho')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao remover produto do carrinho!')
        return redirect(carrinho_user)   
    return redirect(carrinho_user)
    
class fotoproduto(View):
    def get(self, request, proid, multiplo):
        produto = Produto.objects.filter(proid = proid).first()
        if multiplo == 0 or multiplo == 2:
            prffoto = ProdutoFoto.objects.filter(produto_proid = produto.proid).first()   
        else:
            prffoto = ProdutoFoto.objects.filter(produto_proid = produto.proid)
            if len(prffoto) > 1:
                prfprimeira_foto= ProdutoFoto.objects.filter(produto_proid = produto.proid).first() 
                varias = 1
                return render(request, "load_foto_produto.html", {"produto": produto, "proid": proid, "prffoto": prffoto, "multiplo": multiplo, "varias": varias, "prfprimeira_foto": prfprimeira_foto})
        return render(request, "load_foto_produto.html", {"produto": produto, "proid": proid, "prffoto": prffoto, "multiplo": multiplo})
    
@login_required(login_url="/accounts/login")
def petshop_produto_detalhe(request, proid):
    if str(request.user.groups.first()) == 'Pet shop':
        petshop = Petshop.objects.filter(ptsemail = str(request.user.email)).first()
        produto = Produto.objects.filter(proid = proid).first()
        fotos_produto = ProdutoFoto.objects.filter(produto_proid = produto.proid)
        return render(request, 'petshop_detalhes_produto.html', {'produto': produto, 'petshop': petshop, 'fotos_produto': fotos_produto})
    else:
        messages.error(request, 'Usuário deve ser uma loja Pet shop!')
        return render(request, 'index.html')