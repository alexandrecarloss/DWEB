from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login
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

