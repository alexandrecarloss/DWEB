from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login as login_django, logout, authenticate
from django.shortcuts import redirect, get_object_or_404
from django.db import IntegrityError, connection
from adocao.models import Pessoa, Ong, Petshop

cursor = connection.cursor()
# def cadastro_account(request):
#     if request.method == 'GET':
#         return render(request, 'cadastro_tudo.html', {'form': UserCreateForm})
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(request.POST['username'], password= request.POST['password1'])
#                 user.save()
#                 login_django(request, user)
#                 return redirect('index')
#             except IntegrityError:
#                 return render(request, 'cadastro_tudo.html', {'form': UserCreateForm, 'error': 'Usuário já existe. Escolha um novo usuário.'})
#         else:
#             return render(request, 'cadastro_tudo.html', {'form': UserCreateForm, 'error': 'Senhas não coincidem'})


def cadastro_account(request):
    #print('tipo: ', user.groups.name)
    #Verificação do método de acesso
    if request.method == 'GET':
        return render(request, 'cadastro_tudo.html')
    else:
        tipoPessoa = request.POST.get('tipoPessoa')
        #Verificação de confirmação de senha
        if(request.POST['password1'] == request.POST['password2']):
            #Inserir pessoa na tabela pessoa no banco por procedimento
            if tipoPessoa == 'pessoaFisica':
                pescpf = request.POST.get('pescpf')
                pesdtnascto = request.POST.get('pesdtnascto')
                pessexo = request.POST.get('pessexo')
                pescidade = request.POST.get('pescidade')
                pesbairro = request.POST.get('pesbairro')
                pesrua = request.POST.get('pesrua')
                pesemail = request.POST.get('pesemail')
                pesnumero = request.POST.get('pesnumero')
                pestelefone = request.POST.get('pestelefone')
                pesnome = request.POST.get('pesnome')
                pesestado = request.POST.get('pesestado')
                
                antuser = User.objects.filter(username=pesemail).first()
                
                #antuser = get_object_or_404(User, username=pesemail)
                if(antuser):
                    #print('E-mail já cadastrado')
                    return render(request, 'cadastro_tudo.html', {'error': 'Usuário com esse e-mail já existe. Escolha um novo e-mail ou faça login neste.'})
                else:
                    #print('Novo email')
                    try:
                        cursor.execute('call sp_inserepessoa (%(cpf)s, %(dtnascto)s, %(sexo)s, %(cidade)s, %(bairro)s, %(rua)s, %(email)s, %(numero)s, %(telefone)s, %(nome)s, %(estado)s)', {'cpf': pescpf, 'dtnascto': pesdtnascto, 'sexo': pessexo, 'cidade': pescidade, 'bairro': pesbairro, 'rua': pesrua, 'email': pesemail, 'numero': pesnumero, 'telefone': pestelefone, 'nome': pesnome, 'estado': pesestado})
                        result = cursor.fetchall()
                        #print(result)
                    finally:
                        cursor.close()
                    #Cadastro para autenticação
                    try:
                        #grupo = get_list_or_404(Group, name="Pessoa")
                        user = User.objects.create_user(pesemail, password=request.POST['password1'], first_name = pesnome.split()[0])
                        user.groups.add(1)
                        user.save()
                        login_django(request, user)
                        request.session['response'] = "Usuário cadastrado com sucesso!"
                        return redirect('index')
                    except IntegrityError:                   
                        return render(request, 'cadastro_tudo.html', {'error': 'Usuário com esse e-mail já existe. Escolha um novo e-mail ou faça login neste.'})
            elif tipoPessoa == 'ong':
                #Inserir ong no banco
                nomeONG = request.POST.get('nomeONG')
                cidadeONG = request.POST.get('cidadeONG')
                bairroONG = request.POST.get('bairroONG')
                ruaONG = request.POST.get('ruaONG')
                numONG = request.POST.get('numONG')
                telefoneONG = request.POST.get('telefoneONG')
                emailONG = request.POST.get('emailONG')
                antuser = User.objects.filter(username=pesemail).first()
                #antuser = get_object_or_404(User, username=pesemail)
                if(antuser):
                    #print('E-mail já cadastrado')
                    return render(request, 'cadastro_tudo.html', {'error': 'Usuário com esse e-mail já existe. Escolha um novo e-mail ou faça login neste.'})
                else:
                    #print('Novo email')
                    try:
                        Ong.objects.create(ongnome = nomeONG, ongcidade = cidadeONG, ongbairro = bairroONG, ongrua = ruaONG, ongnum = numONG, ongtelefone = telefoneONG, ongemail = emailONG)
                    finally:
                        ongnovo = Ong.objects.order_by('-ongid')[0]
                    #Cadastro para autenticação
                    try:
                        #grupo = get_list_or_404(Group, name="Ong")
                        user = User.objects.create_user(emailONG, password=request.POST['password1'], first_name = nomeONG)
                        user.groups.add(2)
                        user.save()
                        login_django(request, user)
                        request.session['response'] = "Usuário cadastrado com sucesso!"
                        return redirect('index')
                    except IntegrityError:                   
                        return render(request, 'cadastro_tudo.html', {'error': 'Usuário com esse e-mail já existe. Escolha um novo e-mail ou faça login neste.'})

            elif tipoPessoa == 'pessoaJuridica':
                ptsnome = request.POST.get('ptsnome')
                ptscnpj = request.POST.get('ptscnpj')
                ptscidade = request.POST.get('ptscidade')
                ptsbairro = request.POST.get('ptsbairro')
                ptsrua = request.POST.get('ptsrua')
                ptsnumero = request.POST.get('ptsnumero')
                ptstelefone = request.POST.get('ptstelefone')
                ptsemail = request.POST.get('ptsemail')
                #antuser = get_object_or_404(User, username=pesemail)
                antuser = User.objects.filter(username=pesemail).first()
                if(antuser):
                    #print('E-mail já cadastrado')
                    return render(request, 'cadastro_tudo.html', {'error': 'Usuário com esse e-mail já existe. Escolha um novo e-mail ou faça login neste.'})
                else:
                    #print('Novo email')
                    try:
                        Petshop.objects.create(ptsnome = ptsnome, ptscnpj = ptscnpj, ptscidade = ptscidade, ptsbairro = ptsbairro, ptsrua = ptsrua, ptsnumero = ptsnumero, ptstelefone = ptstelefone, ptsemail = ptsemail)
                    finally:
                        petshopnovo = Petshop.objects.order_by('-ptsid')[0]
                        #print(petshopnovo)
                    #Cadastro para autenticação
                    try:
                        #grupo = get_list_or_404(Group, name="Pet shop")
                        user = User.objects.create_user(ptsemail, password=request.POST['password1'], first_name = ptsnome)
                        user.groups.add(3)
                        user.save()
                        login_django(request, user)
                        request.session['response'] = "Usuário cadastrado com sucesso!"
                        return redirect('index')
                    except IntegrityError:                   
                        return render(request, 'cadastro_tudo.html', {'error': 'Usuário com esse e-mail já existe. Escolha um novo e-mail ou faça login neste.'})
        else:
            return render(request, 'cadastro_tudo.html', {'error': 'Senhas não coincidem'})
        
def logoutaccount(request):
    logout(request)
    return redirect('index')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('password')
        user = authenticate(request, username=email, password=senha)
        if user is None:
            return render(request, 'login.html', {'error': 'Usuário e senha não coincidem'})
        else:
            login_django(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')

