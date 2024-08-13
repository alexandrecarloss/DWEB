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
from statistics import mean

token = '8d5dec11c6d81e78b4aaa63bc56a98f53cf6f30e'
headers = {
    'Authorization': f'Token {token}',
    'Content-Type': 'application/json',
}

def produtos(request):
    nome_produto_pesquisa = request.GET.get('nome_produto_pesquisa')
    categorias = CategoriaProduto.objects.all()
    if nome_produto_pesquisa:
         produtos_todos = Produto.objects.all().filter(pronome__icontains = nome_produto_pesquisa)
    else:
        produtos_todos = Produto.objects.all()
    produtos = []
    for p in produtos_todos:
        if p.prosaldo > 0:
            produtos.append(p)
    return render(request, 'pagProdutos.html', {'produtos': produtos, 'categorias': categorias})

def load_produtos_categoria(request):
    id_categoria_pesquisa = request.GET.get('categoria')
    produtos_filtrados = Produto.objects.all().filter(categoria_produto_ctpid = id_categoria_pesquisa)
    produtos = []
    for p in produtos_filtrados:
        if p.prosaldo > 0:
            produtos.append(p)
    return render(request, "load_produtos_categoria.html", {"produtos": produtos})

def servicos(request):
    # current_site = get_current_site(request)
    # mail_subject = "Notificação de compra"
    # message = f'Acesse o site pelo link http://{current_site.domain}/accounts/usuario/'
    # #Envio do e-mail   
    # try:
    #     to_email = 'karurosualexandresouza1234@gmail.com'
    #     email = EmailMessage(
    #         mail_subject, message, to=[to_email], from_email="projeto.artemis@outlook.com"
    #     )
    #     email.send()
    #     print(email)
    # except Exception as  erro:
    #     print('Excessão: ', erro)
    #     messages.error(request, 'Ocorreu um erro ao enviar e-mail')
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
def alteraservico(request, serid):
    cursor = connection.cursor()
    preco = request.POST.get('servalor')
    var_petshop = Petshop.objects.filter(ptsemail = request.user.email).first()
    tipo = request.POST.get('servico')
    descricao = request.POST.get('serdescricao')
    try:
        cursor.execute('call sp_altera_servico (%(preco)s, %(petshop)s, %(tipo)s, %(decsricao)s, %(cod)s)', {
                'preco': preco, 
                'petshop': var_petshop.ptsid, 
                'tipo': tipo, 
                'decsricao': descricao, 
                'cod': serid
            })
        messages.success(request, 'Serviço alterado com sucesso!')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao alterar serviço!')
        return redirect(petshop)
    finally:
        cursor.close()
    return redirect(petshop)

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
    contexto = context_grupo_usuario(request)
    if contexto['dado_usuario'] == None:
        messages.error(request, 'Termine seu cadastro')
        return redirect(cadastro_dados)
    if str(request.user.groups.first()) == 'Pessoa':
        pessoa = Pessoa.objects.filter(pesemail = str(request.user.email)).first()
        produto = Produto.objects.filter(proid = proid).first()
        fotos_produto = ProdutoFoto.objects.filter(produto_proid = produto.proid)
        avaliacoes = Avaliacao.objects.filter(produto_proid = produto)
        media_avaliacoes = 0
        if avaliacoes:
            vetor_avavalor = []
            for avaliacao in avaliacoes:
                vetor_avavalor.append(avaliacao.avavalor)
            media_avaliacoes = int(mean(vetor_avavalor))
        return render(request, 'detalhes_produto_novo.html', {'produto': produto, 'pessoa': pessoa, 'fotos_produto': fotos_produto, 'media_avaliacoes': media_avaliacoes, 'avaliacoes': avaliacoes})
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
    

def checkout_produto(request):
    if str(request.user.groups.all()[0]) == 'Pessoa':
        pessoa = Pessoa.objects.filter(pesemail = request.user.email).first()
        pesid = pessoa.pesid
        carrinhos = Carrinho.objects.filter(carpes = pesid)
        total_carrinhos = 0
        for c in carrinhos:
            total_carrinhos = total_carrinhos + c.carpreco
        return render(request, 'pagina_checkout_novo.html', {'carrinhos': carrinhos, 'total_carrinhos': total_carrinhos, 'pessoa': pessoa})
    else:
        messages.error(request, 'Usuário deve ser uma pessoa física!')
        return render(request, 'index.html')
    
def finaliza_compra(request):
    if request.method == 'POST':
        fpg = request.POST.get('PaymentMethod')
    cursor = connection.cursor()
    try:
        pessoa_id = Pessoa.objects.filter(pesemail = request.user.email).first().pesid
        if not fpg:
            fpg = 3
        cursor.execute('call sp_finaliza_compra (%(pessoa_id)s, %(fpg)s)', {'pessoa_id': pessoa_id, 'fpg': fpg})
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao solicitar compra!')
        return redirect(carrinho_user)
    finally:
        cursor.close()           
        messages.success(request, 'Compra solicitada com sucesso!')
    return redirect(usuario) 

def form_altera_produto(request, proid):
    produto = Produto.objects.filter(proid = proid).first()
    categorias = CategoriaProduto.objects.all()
    return render(request, 'form_altera_produto.html', {'produto': produto, 'categorias': categorias})

def alteraproduto(request, proid):
    cursor = connection.cursor()
    petshop = Petshop.objects.filter(ptsemail = request.user.email).first()
    pronome = request.POST.get('pronome')
    propreco = request.POST.get('propreco')
    prosaldo = request.POST.get('prosaldo')
    categoriaproduto = request.POST.get('categoriaproduto')
    propetshop = petshop.ptsid
    try:
        cursor.execute('call sp_alteraproduto (%(nome)s, %(preco)s, %(saldo)s, %(petshop)s, %(categoria)s, %(cod)s)', 
                {
                    'nome': pronome, 
                    'preco': propreco, 
                    'saldo': prosaldo, 
                    'petshop': propetshop, 
                    'categoria': categoriaproduto, 
                    'cod': proid
                })
        messages.success(request, 'Produto alterado com sucesso!')
    except Exception as erro:
        print('erro: ', erro)
        messages.error(request, 'Erro ao alterar produto!')
        return redirect(index)
    finally:
        cursor.close()
    return redirect(produtos)

    
@login_required(login_url="/accounts/login")
def agendar_servico_pet(request):
    contexto = context_grupo_usuario(request)
    if contexto['dado_usuario'] == None:
        messages.error(request, 'Termine seu cadastro')
        return redirect(cadastro_dados)
    if str(request.user.groups.first()) == 'Pessoa':
        pessoa = Pessoa.objects.filter(pesemail = request.user.email).first()
        pets = Pet.objects.filter(pessoa_pesid = pessoa.pesid)
    else:
        messages.error(request, 'Usuário deve ser uma pessoa!')
        return render(request, 'index.html')
    return render(request, 'agendar_servico_pet.html', {'pets': pets})

def agendar_servico_servico(request):
    pet_selecionado = Pet.objects.filter(petid = request.POST.get('pet')).first()
    tipos_servico = Tiposervico.objects.all()
    return render(request, 'agendar_servico_servico.html', {'tipos_servico': tipos_servico, 'pet_selecionado': pet_selecionado})
    

def agendar_servico_local(request, petid):
    cidade = request.GET.get('cidade')
    pet_selecionado = Pet.objects.filter(petid = petid).first()
    tipo_servico_selecionado = Tiposervico.objects.filter(tpsid = request.POST.get('tipo_servico')).first() 
    if cidade:
        servicos = Servico.objects.filter(tiposervico_tpsid = tipo_servico_selecionado, petshop_ptsid_id__ptscidade__icontains = cidade)
    else:
        servicos = Servico.objects.filter(tiposervico_tpsid = tipo_servico_selecionado)
    return render(request, 'agendar_servico_local.html', {'servicos': servicos, 'pet_selecionado': pet_selecionado, 'tipo_servico_selecionado': tipo_servico_selecionado})

def load_servicos_local(request, petid, tpsid): 
    cidade = request.GET.get('cidade')
    pet_selecionado = Pet.objects.filter(petid = petid).first()
    tipo_servico_selecionado = Tiposervico.objects.filter(tpsid = request.POST.get('tipo_servico')).first()
    if tpsid:
        tipo_servico_selecionado = Tiposervico.objects.filter(tpsid = tpsid).first() 
    if cidade:
        servicos = Servico.objects.filter(tiposervico_tpsid = tipo_servico_selecionado, petshop_ptsid_id__ptscidade__icontains = cidade)
    else:
        servicos = Servico.objects.filter(tiposervico_tpsid = tipo_servico_selecionado)
    return render(request, 'agendar_servico_local.html', {'servicos': servicos, 'pet_selecionado': pet_selecionado, 'tipo_servico_selecionado': tipo_servico_selecionado, 'cidade': cidade})

def agendar_servico_data(request, petid, tpsid):
    pet_selecionado = Pet.objects.filter(petid = petid).first()
    tipo_servico_selecionado = Tiposervico.objects.filter(tpsid = tpsid).first() 
    servico_selecionado = Servico.objects.filter(serid = request.POST.get('servico')).first()
    return render(request, 'agendar_servico_data.html', {'pet_selecionado': pet_selecionado, 'tipo_servico_selecionado': tipo_servico_selecionado, 'servico_selecionado': servico_selecionado})

def agendar_servico_servico_voltar(request, petid):
    pet_selecionado = Pet.objects.filter(petid = petid).first()
    tipos_servico = Tiposervico.objects.all()
    return render(request, 'agendar_servico_servico.html', {'tipos_servico': tipos_servico, 'pet_selecionado': pet_selecionado})

def agendar_servico_local_voltar(request, petid, tpsid):
    cidade = request.GET.get('cidade')
    pet_selecionado = Pet.objects.filter(petid = petid).first()
    tipo_servico_selecionado = Tiposervico.objects.filter(tpsid = tpsid).first() 
    if cidade:
        servicos = Servico.objects.filter(tiposervico_tpsid = tipo_servico_selecionado, petshop_ptsid_id__ptscidade__icontains = cidade)
    else:
        servicos = Servico.objects.filter(tiposervico_tpsid = tipo_servico_selecionado)
    return render(request, 'agendar_servico_local.html', {'servicos': servicos, 'pet_selecionado': pet_selecionado, 'tipo_servico_selecionado': tipo_servico_selecionado})


def solicita_servico(request, petid, serid):
    cursor = connection.cursor()
    data = request.POST.get('date')
    hora = request.POST.get('time')
    datetime = f'{data} {hora}'
    pessoa = Pessoa.objects.filter(pesemail = request.user.email).first()
    try:
        cursor.execute('call sp_insere_solicita (%(pessoa)s, %(servico)s, %(agendamento)s, %(pet)s)', 
            {
                'pessoa': pessoa.pesid, 
                'servico': serid, 
                'agendamento': datetime, 
                'pet': petid, 
            })
        messages.success(request, 'Solicitado com sucesso!')
    except Exception as erro:
        print('erro: ', erro)
        messages.error(request, 'Erro ao solicitar serviço!')
        return redirect(servicos)
    finally:
        cursor.close()
    return redirect(usuario)

def form_altera_servico(request, serid):
    contexto = context_grupo_usuario(request)
    if contexto['dado_usuario'] == None:
        messages.error(request, 'Termine seu cadastro')
        return redirect(cadastro_dados)
    tiposervicos =Tiposervico.objects.all()
    servico = Servico.objects.filter(serid = serid).first()
    return render(request, 'form_altera_servico.html', {'tiposervicos': tiposervicos, 'servico': servico})

def cancelar_solicitacao(request, solid):
    cursor = connection.cursor()
    try:
        cursor.execute('call sp_exclui_solicita (%(cod)s)', {
                'cod': solid
            })
        messages.success(request, 'Solicitação removido com sucesso!')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao remover solicitação!')
    finally:
        cursor.close()
    return redirect(servicos)

####################################  Solicitação por página única não ficou muito bom ###################
tipo_servico_selecionado = 0
def select_cidades_tpservico(request):
    tipo_servico_selecionado = request.GET.get('tipo_servico')
    request.session['tipo_servico_selecionado'] = tipo_servico_selecionado
    cursor = connection.cursor()
    cidades_tpservico = []
    try:
        cursor.execute('call sp_cidade_tpservico (%(tipo_servico)s)', {
                'tipo_servico': tipo_servico_selecionado
            })
        results = cursor.fetchall()
        for c in results:
            cidades_tpservico.append(c[0])
    except Exception as erro:
        print(erro)
    finally:
        cursor.close()
    return render(request, 'cidades_tpservico.html', {'cidades_tpservico': cidades_tpservico, 'tipo_servico_selecionado': tipo_servico_selecionado})
    

def solicitar_servico_junto(request):
    pessoa = Pessoa.objects.filter(pesemail = request.user.email).first()
    pets = Pet.objects.filter(pessoa_pesid = pessoa.pesid)
    tipos_servico = Tiposervico.objects.all()
    return render(request, 'servicos_pag2.html', {'pets': pets, 'tipos_servico': tipos_servico, 'tipo_servico_selecionado': tipo_servico_selecionado})

def load_petshop_cidade(request):
    cidade = request.GET.get('cidade')
    tipo_servico_selecionado = int(request.session['tipo_servico_selecionado'])
    print('cedade, tps selecionada', cidade, tipo_servico_selecionado)
    servicos = Servico.objects.filter(tiposervico_tpsid = tipo_servico_selecionado)
    if cidade:
        servicos = Servico.objects.filter(tiposervico_tpsid = tipo_servico_selecionado, petshop_ptsid__ptscidade__icontains = cidade)
    return render(request, 'load_petshop_cidade.html', {'servicos': servicos, 'tipo_servico_selecionado': tipo_servico_selecionado})

def solicita_servico_junto(request):
    servico_selecionado = Servico.objects.filter(serid = request.POST.get('servico')).first()
    pet_selecionado = Pet.objects.filter(petid = request.POST.get('pet')).first()
    cursor = connection.cursor()
    data = request.POST.get('date')
    hora = request.POST.get('time')
    datetime = f'{data} {hora}'
    pessoa = Pessoa.objects.filter(pesemail = request.user.email).first()
    try:
        cursor.execute('call sp_insere_solicita (%(pessoa)s, %(servico)s, %(agendamento)s, %(pet)s)', 
            {
                'pessoa': pessoa.pesid, 
                'servico': servico_selecionado.serid, 
                'agendamento': datetime, 
                'pet': pet_selecionado.petid, 
            })
        messages.success(request, 'Solicitado com sucesso junto!')
    except Exception as erro:
        print('erro: ', erro)
        messages.error(request, 'Erro ao solicitar serviço!')
        return redirect(servicos)
    finally:
        cursor.close()
    return redirect(usuario)

##################### Fim solicita junto

@login_required(login_url="/accounts/login")
def usuario_produto_detalhe(request, proid):
    if str(request.user.groups.first()) == 'Pessoa':
        petshop = Petshop.objects.filter(ptsemail = str(request.user.email)).first()
        produto = Produto.objects.filter(proid = proid).first()
        fotos_produto = ProdutoFoto.objects.filter(produto_proid = produto.proid)
        avaliacoes = Avaliacao.objects.filter(produto_proid = produto)
        media_avaliacoes = 0
        if avaliacoes:
            vetor_avavalor = []
            for avaliacao in avaliacoes:
                vetor_avavalor.append(avaliacao.avavalor)
            media_avaliacoes = int(mean(vetor_avavalor))
        return render(request, 'usuario_detalhes_produto.html', {'produto': produto, 'petshop': petshop, 'fotos_produto': fotos_produto, 'avaliacoes': avaliacoes, 'media_avaliacoes': media_avaliacoes})
    else:
        messages.error(request, 'Usuário deve ser uma pessoa!')
        return render(request, 'index.html')


@login_required(login_url="/accounts/login")
def insere_avaliacao_produto(request, proid):
    cursor = connection.cursor()
    if str(request.user.groups.first()) == 'Pessoa':
        avadescricao = request.POST.get('avadescricao')
        avavalor = request.POST.get('avavalor')
        pessoa = Pessoa.objects.filter(pesemail = request.user.email).first()
        print(avavalor)
        try:
            cursor.execute('call sp_insere_avaliacao (%(produto)s, %(servico)s, %(descricao)s, %(valor)s, %(pessoa)s)', 
                {
                    'produto': proid, 
                    'servico': None,
                    'descricao': avadescricao, 
                    'valor': avavalor, 
                    'pessoa': pessoa.pesid 
                })
            messages.success(request, 'Avaliado com sucesso!')
        except Exception as erro:
            print('erro: ', erro)
            messages.error(request, 'Erro ao avaliar!')
            return redirect(usuario)
        finally:
            cursor.close()
        return redirect(usuario)
    else:
        messages.error(request, 'Usuário deve ser uma pessoa!')
        return render(request, 'index.html')
    
@login_required(login_url="/accounts/login")
def insere_avaliacao_servico(request, serid):
    cursor = connection.cursor()
    if str(request.user.groups.first()) == 'Pessoa':
        avadescricao = request.POST.get('avadescricao')
        avavalor = request.POST.get('avavalor')
        pessoa = Pessoa.objects.filter(pesemail = request.user.email).first()
        
        try:
            cursor.execute('call sp_insere_avaliacao (%(produto)s, %(servico)s, %(descricao)s, %(valor)s, %(pessoa)s)', 
                {
                    'produto': None, 
                    'servico': serid,
                    'descricao': avadescricao, 
                    'valor': avavalor, 
                    'pessoa': pessoa.pesid 
                })
            messages.success(request, 'Avaliado com sucesso!')
        except Exception as erro:
            print('erro: ', erro)
            messages.error(request, 'Erro ao avaliar!')
            return redirect(usuario)
        finally:
            cursor.close()
        return redirect(usuario)
    else:
        messages.error(request, 'Usuário deve ser uma pessoa!')
        return render(request, 'index.html')
    
@login_required(login_url="/accounts/login")
def exclui_avaliacao(request, avacod):
    cursor = connection.cursor()
    if str(request.user.groups.first()) == 'Pessoa':
        try:
            cursor.execute('call sp_exclui_avaliacao (%(cod)s)', 
                {
                    'cod': avacod
                })
            messages.success(request, 'Avaliação excluída com sucesso!')
        except Exception as erro:
            print('erro: ', erro)
            messages.error(request, 'Erro ao excluir avaliação!')
            return redirect(usuario)
        finally:
            cursor.close()
        return redirect(usuario)
    else:
        messages.error(request, 'Usuário deve ser uma pessoa!')
        return render(request, 'index.html')
    

@login_required(login_url="/accounts/login")
def altera_avaliacao(request, avacod):
    cursor = connection.cursor()
    if str(request.user.groups.first()) == 'Pessoa':
        avadescricao = request.POST.get('avadescricao')
        avavalor = request.POST.get('avavalor')
        try:
            cursor.execute('call sp_insere_avaliacao (%(avadescricao)s, %(avavalor)s, %(cod)s)', 
                {
                    'avadescricao': avadescricao, 
                    'avavalor': avavalor, 
                    'cod': avacod 
                })
            messages.success(request, 'Avaliação alterada com sucesso!')
        except Exception as erro:
            print('erro: ', erro)
            messages.error(request, 'Erro ao alterar avaliação!')
            return redirect(usuario)
        finally:
            cursor.close()
        return redirect(usuario)
    else:
        messages.error(request, 'Usuário deve ser uma pessoa!')
        return render(request, 'index.html')
    
def aceitar_solicitacao(request, solid):
    cursor = connection.cursor()
    try:
        cursor.execute('call sp_altera_status_solicita (%(cod)s, %(novo)s)', {
                'cod': solid,
                'novo': 'Concluído'
            })
        messages.success(request, 'Solicitação aceita com sucesso!')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao aceitar solicitação!')
    finally:
        cursor.close()
    return redirect(servicos)

def negar_solicitacao(request, solid):
    cursor = connection.cursor()
    try:
        cursor.execute('call sp_altera_status_solicita (%(cod)s, %(novo)s)', {
                'cod': solid,
                'novo': 'Cancelado'
            })
        messages.success(request, 'Solicitação cancelada com sucesso!')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao cancelar solicitação!')
    finally:
        cursor.close()
    return redirect(servicos)