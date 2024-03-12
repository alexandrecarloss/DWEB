from django.shortcuts import render
from django.http import HttpResponse
from .models import petteste

def home(request):
    pets = petteste.objects.all()
    return render(request, 'home.html', {'Pet': petteste})

def about(request):
    return render(request, 'about.html')
# Create your views here.
