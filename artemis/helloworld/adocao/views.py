from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pet, PetRaca, PetTipo, PetFoto, Pessoa
from .forms import especieForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def adocao(request):
    form = especieForm()
    nomePesquisa = request.GET.get('nomepesquisa')
    especie = request.GET.get('especie')
    raca = request.GET.get('raca')
    pettipos = PetTipo.objects.all()
    pessoas = Pessoa.objects.all()
    if nomePesquisa:
        pets = Pet.objects.filter(petnome__icontains=nomePesquisa)
    elif especie:
        if raca:
            pets = Pet.objects.filter(pet_raca_ptrid = raca)
        else:
            pets = Pet.objects.filter(pet_tipo_pttid = especie)
    else:
        pets = Pet.objects.all()
    pftfotos = PetFoto.objects.all()
    return render(request, 'adocao.html', {'pets': pets, 'pettipos': pettipos, 'form': form, 'pftfotos': pftfotos, "pessoas": pessoas, "especie": especie, "raca": raca, "nomePesquisa": nomePesquisa})

def load_racas(request):
    id_specie = request.GET.get('especie')
    racas = PetRaca.objects.filter(pet_tipo_pttid = id_specie)
    return render(request, "raca_options.html", {"racas": racas})

def load_pets(request):
    especie = request.GET.get('especie')
    raca = request.GET.get('raca')  
    if raca:
        pets = Pet.objects.filter(pet_raca_ptrid = raca)
    else:
        pets = Pet.objects.all()
    pftfotos = PetFoto.objects.all()
    
    return render(request, "load_pets.html", {"pets": pets, "raca": raca, "pftfotos": pftfotos, "especie": especie})

def petdetalhe(request):
    return render(request, "pagDetalheAdocao.html")
