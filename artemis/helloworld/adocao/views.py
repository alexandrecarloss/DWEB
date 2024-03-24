from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pet, PetRaca, PetTipo, PetFoto, Pessoa, PetPorte
from .forms import especieForm
from django.views import View

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

class petdetalhe(View):
    def get(self, request, petid):
        pet = Pet.objects.filter(petid = petid).first()
        pftfotos = PetFoto.objects.filter(pet_petid = petid)
        return render(request, "pagDetalheAdocao.html", {"pet": pet, "petid": petid, "pftfotos": pftfotos})
    
def cadastropet(request):
    return render(request, "pagCadastroPet.html")

def salvarpet(request):
    petnome = request.POST.get('petnome')
    petsexo = request.POST.get('petsexo')
    petcastrado = request.POST.get('petcastrado')
    petdtnascto = request.POST.get('petdtnascto')
    petpeso = request.POST.get('petpeso')
    pessoa_pesid = request.POST.get('petsexo')
    pet_porte_ptpid = request.POST.get('petporte')
    pet_raca_ptrid = request.POST.get('petraca')
    pet_tipo_pttid = request.POST.get('pettipo')

    
    porte = PetPorte.objects.filter(ptpid = pet_porte_ptpid).first()
    raca = PetRaca.objects.filter(ptrid = pet_raca_ptrid).first()
    tipo = PetTipo.objects.filter(pttid = pet_tipo_pttid).first()


    Pet.objects.create(petnome = petnome, petsexo = petsexo, petcastrado = petcastrado, petdtnascto = petdtnascto, petpeso = petpeso, pet_porte_ptpid = porte, pet_raca_ptrid = raca, pet_tipo_pttid = tipo)

    return render(request, "adocao.html")
