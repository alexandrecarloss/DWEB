from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet, PetRaca, PetTipo

def home(request):
    return render(request, 'index.html')

def adocao(request):
    pets = Pet.objects.all()
    pettipos = PetTipo.objects.all()
    petracas = PetRaca.objects.all().select_related('pet_tipo_pttid')
    return render(request, 'adocao.html', {'pets': pets, 'petracas': petracas, 'pettipos': pettipos})

def about(request):
    return render(request, 'about.html')

def vizualizarpet(request, Pet):
    return render(request, 'vizualizarpet.html', {'Pet': Pet})
# Create your views here.
