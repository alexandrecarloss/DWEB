from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet, PetRaca, PetTipo

def home(request):
    return render(request, 'home.html')

def adocao(request):
    pets = Pet.objects.all()
    pettipos = PetTipo.objects.all()
    petracas = PetRaca.objects.filter(pet_tipo_pttid = 1)
    return render(request, 'adocao.html', {'pets': pets, 'petracas': petracas, 'pettipos': pettipos})
    #pets = petteste.objects.all()
    #pets = pet.objects.all()
    #return render(request, 'home.html', {'pets': pets})

def about(request):
    return render(request, 'about.html')
# Create your views here.
