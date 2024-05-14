from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreateForm, RegistrationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login as login_django, logout, authenticate, get_user_model
from django.shortcuts import redirect, get_object_or_404
from django.db import IntegrityError, connection
from adocao.models import Pessoa, Ong, Petshop
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
from django.contrib.auth.decorators import login_required
from adocao.models import Pet, PetRaca, PetTipo, PetFoto, Pessoa, PetPorte, PetAdocao,Ong

################# Accountsdjango

def register_user(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = "Ative sua conta"
            message = render_to_string("account_activate_email.html", { 
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user)
            })
            try:
                to_email = form.cleaned_data.get("email")
                email = EmailMessage(
                    mail_subject, message, to=[to_email], from_email="projeto.artemis@outlook.com"
                )
                email.send()
                messages.success(request, "Por favor, cheque seu e-mail para completar o registro.")               
            finally:
                return redirect("index")
    return render(request, "register.html", {"form": form})    

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        login_django(request, user)
        messages.success(request, 'Sua conta foi ativada com sucesso!')
        return redirect("loginaccount")
    else:
        messages.error(request, "O link de ativação é inválido ou expirou")
        return redirect("index")

################# Fim accounts


def cadastro_account(request):
    cursor = connection.cursor()
    mensagens_para_exibir = messages.get_messages(request)
    #print('tipo: ', user.groups.name)
    #Verificação do método de acesso
    if request.method == 'GET':
        return render(request, 'cadastro_tudo.html')
    else:
        tipoPessoa = request.POST.get('tipoPessoa')
        #Verificação de confirmação de senha
        if(request.POST['password1'] == request.POST['password2']):
            #Verificação do tipo de cadastro
            if tipoPessoa == 'pessoaFisica':
                pescpf = request.POST.get('pescpf')
                pescpf = re.sub('[^a-zA-Z0-9]', '', pescpf)
                pesdtnascto = request.POST.get('pesdtnascto')
                pessexo = request.POST.get('pessexo')
                pescidade = request.POST.get('pescidade')
                pesbairro = request.POST.get('pesbairro')
                pesrua = request.POST.get('pesrua')
                pesemail = request.POST.get('pesemail')
                pesnumero = request.POST.get('pesnumero')
                pestelefone = request.POST.get('pestelefone')
                pestelefone = re.sub('[^a-zA-Z0-9]', '', pestelefone)
                pesnome = request.POST.get('pesnome')
                pesestado = request.POST.get('pesestado')
                first_name = pesnome.split()[0]
                antuser = User.objects.filter(email=pesemail).first()
                #antuser = get_object_or_404(User, username=pesemail)
                if(antuser):
                    messages.error(request, 'Usuário com esse e-mail já existe. Escolha um novo e-mail ou faça login neste.')
                    return render(request, 'cadastro_tudo.html', {"messages": mensagens_para_exibir})
                else:                   
                    #Cadastro para autenticação
                    try:
                        senha = request.POST['password1']
                        #grupo = get_list_or_404(Group, name="Pessoa")
                        print(first_name, senha, pesemail)                        
                        user = User.objects.create_user(pesemail, password=senha, first_name = first_name, email=pesemail)
                        print('aqui')
                        user.groups.add(1)
                        user.save()
                        #Envio de email
                        # current_site = get_current_site(request)
                        # mail_subject = "Ative sua conta"
                        # message = render_to_string("account_activate_email.html", { 
                        #     "user": user,
                        #     "domain": current_site.domain,
                        #     "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        #     "token": account_activation_token.make_token(user)
                        # })
                        # try:
                        #     to_email = request.POST.get('pesemail')
                        #     email = EmailMessage(
                        #         mail_subject, message, to=[to_email], from_email="projeto.artemis@outlook.com"
                        #     )
                        #     email.send()
                        #     messages.success(request, "Por favor, cheque seu e-mail e caixa de spam para completar o registro.")               
                        # finally:
                        #     #login_django(request, user)
                        #     messages.success(request, 'Usuário cadastrado com sucesso!')
                        #Inserindo objeto no banco
                        try:
                            #Verificando se alterar ou inserir
                            antpessoa = Pessoa.objects.filter(pesemail = pesemail).first()
                            if antpessoa:
                                cursor.execute('call sp_alterapessoa (%(cpf)s, %(dtnascto)s, %(sexo)s, %(cidade)s, %(bairro)s, %(rua)s, %(email)s, %(numero)s, %(telefone)s, %(nome)s, %(estado)s, %(cod)s)', {'cpf': pescpf, 'dtnascto': pesdtnascto, 'sexo': pessexo, 'cidade': pescidade, 'bairro': pesbairro, 'rua': pesrua, 'email': pesemail, 'numero': pesnumero, 'telefone': pestelefone, 'nome': pesnome, 'estado': pesestado, 'cod': antpessoa.pesid})
                            else:
                                cursor.execute('call sp_inserepessoa (%(cpf)s, %(dtnascto)s, %(sexo)s, %(cidade)s, %(bairro)s, %(rua)s, %(email)s, %(numero)s, %(telefone)s, %(nome)s, %(estado)s)', {'cpf': pescpf, 'dtnascto': pesdtnascto, 'sexo': pessexo, 'cidade': pescidade, 'bairro': pesbairro, 'rua': pesrua, 'email': pesemail, 'numero': pesnumero, 'telefone': pestelefone, 'nome': pesnome, 'estado': pesestado})
                                result = cursor.fetchall()
                        finally:
                            cursor.close()
                            #login_django(request, user)
                            messages.success(request, 'Usuário cadastrado com sucesso!')
                    except Exception as  erro:
                        print('Excessão: ', erro)
                    finally:
                        return redirect("loginaccount")
            elif tipoPessoa == 'ong':
                #Inserir ong no banco
                nomeONG = request.POST.get('nomeONG')
                cidadeONG = request.POST.get('cidadeONG')
                bairroONG = request.POST.get('bairroONG')
                ruaONG = request.POST.get('ruaONG')
                numONG = request.POST.get('numONG')
                telefoneONG = request.POST.get('telefoneONG')
                telefoneONG = re.sub('[^a-zA-Z0-9]', '', telefoneONG)
                emailONG = request.POST.get('emailONG')
                ongestado = request.POST.get('ongestado')
                antuser = User.objects.filter(email=emailONG).first()
                #antuser = get_object_or_404(User, username=pesemail)
                if(antuser):
                    messages.error(request, 'Usuário com esse e-mail já existe. Escolha um novo e-mail ou faça login neste.')
                    return render(request, 'cadastro_tudo.html', {"messages": mensagens_para_exibir})
                else:                   
                    try:
                        #Cadastro para autenticação
                        #grupo = get_list_or_404(Group, name="Ong")
                        user = User.objects.create_user(emailONG, password=request.POST['password1'], first_name = nomeONG, email=emailONG)
                        user.groups.add(2)
                        user.save()
                        ####   Envio de email
                        # current_site = get_current_site(request)
                        # mail_subject = "Ative sua conta"
                        # message = render_to_string("account_activate_email.html", { 
                        #     "user": user,
                        #     "domain": current_site.domain,
                        #     "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        #     "token": account_activation_token.make_token(user)
                        # })
                        # try:
                        #     to_email = request.POST.get('emailONG')
                        #     email = EmailMessage(
                        #         mail_subject, message, to=[to_email], from_email="projeto.artemis@outlook.com"
                        #     )
                        #     email.send()
                        #     messages.success(request, "Por favor, cheque seu e-mail e caixa de spam para completar o registro.")               
                        # finally:                           
                        #     #login_django(request, user)
                        #     messages.success(request, 'Usuário cadastrado com sucesso!')
                        #Inserindo objeto no banco
                        try:
                            ant_ong = Ong.objects.filter(ongemail = emailONG).first()
                            #Verificar se inserir ou alterar ong
                            if ant_ong:
                                ant_ong.ongnome = nomeONG
                                ant_ong.ongcidade = cidadeONG
                                ant_ong.ongbairro = bairroONG
                                ant_ong.ongrua = ruaONG
                                ant_ong.ongnum = numONG
                                ant_ong.ongtelefone = telefoneONG
                                ant_ong.ongemail = emailONG
                                
                                ant_ong.save()
                            else:
                                Ong.objects.create(ongnome = nomeONG, ongcidade = cidadeONG, ongbairro = bairroONG, ongrua = ruaONG, ongnum = numONG, ongtelefone = telefoneONG, ongemail = emailONG, ongestado = ongestado) 
                                #cursor.execute('call sp_insere_ong (%(nome)s, %(cidade)s, %(bairro)s, %(rua)s, %(num)s, %(telefone)s, %(email)s)', {'nome': nomeONG, 'cidade': cidadeONG, 'bairro': bairroONG, 'rua': ruaONG, 'num': numONG, 'telefone': telefoneONG, 'email': emailONG})
                                #result = cursor.fetchall()
                        except Exception as erro:
                            print("Erro: ", erro) 
                        finally:
                            cursor.close()
                        ongnovo = Ong.objects.order_by('-ongid')[0]
                        messages.success(request, 'Usuário cadastrado com sucesso!')
                    finally:
                        return redirect("loginaccount")
              
            elif tipoPessoa == 'pessoaJuridica':
                ptsnome = request.POST.get('ptsnome')
                ptscnpj = request.POST.get('ptscnpj')
                ptscnpj = re.sub('[^a-zA-Z0-9]', '', ptscnpj)
                ptscidade = request.POST.get('ptscidade')
                ptsbairro = request.POST.get('ptsbairro')
                ptsrua = request.POST.get('ptsrua')
                ptsnumero = request.POST.get('ptsnumero')
                ptstelefone = request.POST.get('ptstelefone')
                ptstelefone = re.sub('[^a-zA-Z0-9]', '', ptstelefone)
                ptsemail = request.POST.get('ptsemail')
                ptsestado = request.POST.get('ptsestado')
                antuser = User.objects.filter(email=ptsemail).first()
                if(antuser):
                    messages.error(request, 'Usuário com esse e-mail já existe. Escolha um novo e-mail ou faça login neste.')
                    return render(request, 'cadastro_tudo.html', {"messages": mensagens_para_exibir})
                else:
                    try:
                        #Cadastro para autenticação
                        user = User.objects.create_user(ptsemail, password=request.POST['password1'], first_name = ptsnome, email=ptsemail)
                        user.groups.add(3)

                        # Envio de email
                        # current_site = get_current_site(request)
                        # mail_subject = "Ative sua conta"
                        # message = render_to_string("account_activate_email.html", { 
                        #     "user": user,
                        #     "domain": current_site.domain,
                        #     "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        #     "token": account_activation_token.make_token(user)
                        # })
                        # try:
                        #     to_email = ptsemail
                        #     email = EmailMessage(
                        #         mail_subject, message, to=[to_email], from_email="projeto.artemis@outlook.com"
                        #     )
                        #     email.send()
                        #     messages.success(request, "Por favor, cheque seu e-mail e caixa de spam para completar o registro.")               
                        # finally:
                        #login_django(request, user)
                        messages.success(request, 'Usuário cadastrado com sucesso!')
                    finally:
                        #Inserindo objeto no banco
                        
                        ant_pet_shop = Petshop.objects.filter(ptsemail = ptsemail).first()
                        if ant_pet_shop:
                            ant_pet_shop.ptsnome = ptsnome
                            ant_pet_shop.ptscnpj = ptscnpj
                            ant_pet_shop.ptscidade = ptscidade
                            ant_pet_shop.ptsbairro = ptsbairro
                            ant_pet_shop.ptsrua = ptsrua
                            ant_pet_shop.ptsnumero = ptsnumero
                            ant_pet_shop.ptstelefone = ptstelefone
                            ant_pet_shop.ptsemail = ptsemail
                            ant_pet_shop.ptsestado = ptsestado
                            ant_pet_shop.save()
                        else:
                            Petshop.objects.create(ptsnome = ptsnome, ptscnpj = ptscnpj, ptscidade = ptscidade, ptsbairro = ptsbairro, ptsrua = ptsrua, ptsnumero = ptsnumero, ptstelefone = ptstelefone, ptsemail = ptsemail, ptsestado = ptsestado)    
                            #cursor.execute('call sp_insere_petshop (%(nome)s, %(cnpj)s, %(cidade)s, %(bairro)s, %(rua)s, %(num)s, %(telefone)s, %(email)s)', {'nome': ptsnome, 'cnpj': ptscnpj, 'cidade': ptscidade, 'bairro': ptsbairro, 'rua': ptsrua, 'num': ptsnumero, 'telefone': ptstelefone, 'email': ptsemail})
                            #result = cursor.fetchall()
                        
                        cursor.close()
                        return redirect('loginaccount')                          
        else:
            messages.error(request, 'Senhas não coincidem')                
            return render(request, 'cadastro_tudo.html', {"messages": mensagens_para_exibir})
                
def logoutaccount(request):
    logout(request)
    return redirect('index')

def loginaccount(request):
    mensagens_para_exibir = messages.get_messages(request)
    if request.method == 'GET':
        return render(request, 'login.html', {"messages": mensagens_para_exibir})
    else:
        email = request.POST.get('email')
        senha = request.POST.get('password')
        user = authenticate(request, username=email, password=senha)
        if user is None:
            return render(request, 'login.html', {'error': 'Usuário e senha não coincidem', "messages": mensagens_para_exibir})
        else:
            login_django(request, user)
            request.session['grupo_usuario'] = str(request.user.groups.all().first())
            #grupo_usuario = request.user.groups.all().first()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')
            
#Redefinição de senha
def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email = email)
            current_site = get_current_site(request)
            mail_subject = "Redefinição de senha"
            message = render_to_string("password_reset_email.html", { 
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user)
            })
            try:
                to_email = email
                email = EmailMessage(
                    mail_subject, message, to=[to_email], from_email="projeto.artemis@outlook.com"
                )
                email.send()
                messages.success(request, "Por favor, cheque seu e-mail e caixa de spam para continuar.")
                return redirect('password_reset_done')
            except Exception as erro:
                print('O erro encontrado foi: ', erro.__cause__)
                messages.error(request, 'Houve um erro ao enviar o e-mail, verifique se o e-mail informado é válido.')
                return render(request, 'password_reset_form.html')
        except Exception as erro:
            print('O erro encontrado foi: ', erro.__cause__)
            messages.error(request, 'Esse endereço de e-mail não é válido, verifique se o e-mail informado é um e-mail cadastrado.')
            return render(request, 'password_reset_form.html')
    else:
        return render(request, 'password_reset_form.html')


def password_reset_done(request):
    return render(request, 'password_reset_done.html')


def password_reset_confirm(request, uidb64, token):
    if request.method == 'POST':
        User = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                user.set_password(password1)
                user.save()

                #login_django(request, user)
                messages.success(request, 'Sua senha foi atualizada com sucesso!')
                return redirect("reset_complete")
            else:
                messages.error(request, 'As senhas não coincidem!')
                return render(request, 'password_reset_confirm.html')
        else:
            messages.error(request, "O link de ativação é inválido ou expirou")
            return redirect("password_reset")
    else: 
        return render(request, 'password_reset_confirm.html')
    
def reset_complete(request):
    return render(request, 'password_reset_complete.html')

@login_required(login_url="/accounts/login")
def usuario(request):
    pettipos = PetTipo.objects.all()
    petportes = PetPorte.objects.all()
    #pet = Pet.objects.filter(petid = petid).first()
    #petfoto = PetFoto.objects.filter(pet_petid = petid).first()
    pesid = Pessoa.objects.filter(pesemail = request.user.email).first().pesid
    #print('email user ', request.user.email)
    pets = Pet.objects.filter(pessoa_pesid = pesid)
    pftfotos = PetFoto.objects.all()
    pessoa = Pessoa.objects.filter(pesemail = request.user.email).first()
    return render(request, "petUsuario.html", {"pets": pets, "pftfotos": pftfotos, "pettipos": pettipos, "petportes": petportes, "pessoa": pessoa})

@login_required(login_url="/accounts/login")
def ong(request):
    pets = []
    pettipos = PetTipo.objects.all()
    petportes = PetPorte.objects.all()
    ong = Ong.objects.filter(ongemail = request.user.email).first()
    ongid = ong.ongid
    pets_adocao = PetAdocao.objects.filter(ong_ongid = ongid)
    # Obtendo os pets que possuem relação com a ong 
    for adocao in pets_adocao:
        pet = Pet.objects.filter(petid = adocao.pet_petid.petid).first()
        pets.append(pet)
    #     print('pet:', pet, 'pets: ', pets)
    # print('Pets query aqui: ', pets)
    return render(request, 'pagOng.html', {'pets': pets, 'pettipos': pettipos, 'petportes': petportes, 'ong': ong})

def atualizar_pessoa(request, pesid):
    if request.method == 'POST':
        try:
            pessoa = Pessoa.objects.filter(pesid = pesid).first()
            user = User.objects.filter(email = pessoa.pesemail).first()
            pessoa.pescpf = request.POST.get('pescpf')
            pessoa.pescpf = re.sub('[^a-zA-Z0-9]', '', pessoa.pescpf)
            pessoa.pesdtnascto = request.POST.get('pesdtnascto')
            pessoa.pessexo = request.POST.get('pessexo')
            pessoa.pescidade = request.POST.get('pescidade')
            pessoa.pesbairro = request.POST.get('pesbairro')
            pessoa.pesrua = request.POST.get('pesrua')
            pessoa.pesemail = request.POST.get('pesemail')
            pessoa.pesnumero = request.POST.get('pesnumero')
            pessoa.pestelefone = request.POST.get('pestelefone')
            pessoa.pestelefone = re.sub('[^a-zA-Z0-9]', '', pessoa.pestelefone)
            pessoa.pesnome = request.POST.get('pesnome')
            pessoa.pesestado = request.POST.get('pesestado')
            pessoa.save()
            
            user.username = pessoa.pesemail
            user.email = pessoa.pesemail
            user.save()
            messages.success(request, 'Dados atualizados com sucesso!')
        except Exception as erro:
            print('Erro: ', erro)
            messages.error(request, 'Erro ao atualizar dados!')
    return redirect('index')

def atualizar_ong(request, ongid):
    if request.method == 'POST':
        try:
            ong = Ong.objects.filter(ongid = ongid).first()
            user = User.objects.filter(email = ong.ongemail).first()
            ong.ongnome = request.POST.get('nomeONG')
            ong.ongcidade = request.POST.get('cidadeONG')
            ong.ongbairro = request.POST.get('bairroONG')
            ong.ongrua = request.POST.get('ruaONG')
            ong.ongnum = request.POST.get('numONG')
            telefoneONG = request.POST.get('telefoneONG')
            ong.ongtelefone = re.sub('[^a-zA-Z0-9]', '', telefoneONG)
            ong.ongemail = request.POST.get('emailONG')
            ong.ongestado = request.POST.get('ongestado')
            ong.save()

            user.username = ong.ongemail
            user.email = ong.ongemail
            user.save()
            messages.success(request, 'Dados atualizados com sucesso!')
        except Exception as erro:
            print('Erro: ', erro)
            messages.error(request, 'Erro ao atualizar dados!')
    return redirect('index')
    