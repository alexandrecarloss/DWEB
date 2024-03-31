from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError

def cadastropessoa(request):
    if request.method == 'GET':
        return render(request, 'cadastropessoa.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password= request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'cadastropessoa.html', {'form': UserCreateForm, 'error': 'Usuário já existe. Escolha um novo usuário.'})
        else:
            return render(request, 'cadastropessoa.html', {'form': UserCreateForm, 'error': 'Senhas não coincidem'})

def cadastro(request):
    if request.method == 'GET':
        print('get')
        return render(request, 'cadastro2.html', {'form': UserCreateForm})
    else:
        print('post')
        if request.POST['password'] == request.POST['confirmPassword']:
            try:
                user = User.objects.create_user(request.POST['name'], password= request.POST['password'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'cadastro2.html', {'form': UserCreateForm, 'error': 'Usuário já existe. Escolha um novo usuário.'})
        else:
            return render(request, 'cadastro2.html', {'form': UserCreateForm, 'error': 'Senhas não coincidem'})
        
def logoutaccount(request):
    logout(request)
    return redirect('index')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {'form': AuthenticationForm(), 'error': 'Usuário e senha não coincidem'})
        else:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')

