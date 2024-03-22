from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pet, PetRaca, PetTipo, PetFoto
from .forms import especieForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def adocao(request):
    form = especieForm()
    pettipos = PetTipo.objects.all()
    pets = Pet.objects.all().select_related
    pftfotos = PetFoto.objects.filter(pet_petid = 1)
    return render(request, 'adocao.html', {'pets': pets, 'pettipos': pettipos, 'form': form, 'pftfotos': pftfotos})

def load_racas(request):
    id_specie = request.GET.get('especie')
    racas = PetRaca.objects.filter(pet_tipo_pttid = id_specie)
    return render(request, "raca_options.html", {"racas": racas})

def load_pets(request):
    #id_specie = request.GET.get('especie')
    raca = request.GET.get('raca')
    pets = Pet.objects.filter(pet_raca_ptrid = raca)
    pftfotos = PetFoto.objects.filter(pet_petid = 1)
    return render(request, "load_pets.html", {"pets": pets, "raca": raca, "pftfotos": pftfotos})

def petdetalhe(request):
    return render(request, "adocaodetails.html")