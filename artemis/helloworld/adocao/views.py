from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Pet, PetRaca, PetTipo, PetFoto, Pessoa, PetPorte
from .forms import especieForm
from django.views import View
from django.db.models import Max
from PIL import Image
import os
from django.conf import settings
from datetime import date
from django.contrib.auth.decorators import login_required
from accounts import views as viewsAccount

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
    return render(request, "raca_options.html", {"racas": racas, "id_specie": id_specie})

def load_pets(request):
    especie = request.GET.get('especie')
    raca = request.GET.get('raca')  
    if raca:
        pets = Pet.objects.filter(pet_raca_ptrid = raca)
    elif especie:
        pets = Pet.objects.filter(pet_tipo_pttid = especie)
    else:
        pets = Pet.objects.all()
    pftfotos = PetFoto.objects.all()
    return render(request, "load_pets.html", {"pets": pets, "raca": raca, "pftfotos": pftfotos, "especie": especie})

@login_required(login_url="/accounts/login")
def petdetalhe(request, petid):
    pet = Pet.objects.filter(petid = petid).first()
    today = date.today() 
    petidade = today.year - pet.petdtnascto.year - ((today.month, today.day) < (pet.petdtnascto.month, pet.petdtnascto.day))
    pftfotos = PetFoto.objects.filter(pet_petid = pet.petid)
    return render(request, "pagDetalheAdocao.html", {"pet": pet, "petid": petid, "pftfotos": pftfotos, "petidade": petidade})
    
class fotopet(View):
    def get(self, request, petid, multiplo):
        pet = Pet.objects.filter(petid = petid).first()
        if multiplo == 0:
            pftfoto = PetFoto.objects.filter(pet_petid = pet.petid).first()
        else:
            pftfoto = PetFoto.objects.filter(pet_petid = pet.petid)
            if len(pftfoto) > 1:
                pftfotoprimeira = PetFoto.objects.filter(pet_petid = pet.petid).first()
                varias = 1
                return render(request, "load_foto_pet.html", {"pet": pet, "petid": petid, "pftfoto": pftfoto, "multiplo": multiplo, "varias": varias, "pftfotoprimeira": pftfotoprimeira})
        return render(request, "load_foto_pet.html", {"pet": pet, "petid": petid, "pftfoto": pftfoto, "multiplo": multiplo})

def cadastropet(request):
    pettipos = PetTipo.objects.all()
    petportes = PetPorte.objects.all()
    return render(request, "pagCadastroPet.html", {"pettipos": pettipos, "petportes": petportes})

def salvarpet(request):
    petnome = request.POST.get('petnome')
    petsexo = request.POST.get('petsexo')
    petcastrado = request.POST.get('petcastrado')
    petdtnascto = request.POST.get('petdtnascto')
    petpeso = request.POST.get('petpeso')
    #pessoa_pesid = request.POST.get('petsexo')
    vpet_porte_ptpid = request.POST.get('petporte')
    vpet_raca_ptrid = request.POST.get('petraca')
    vpet_tipo_pttid = request.POST.get('especie')

    porte = PetPorte.objects.filter(ptpid = vpet_porte_ptpid).first()
    raca = PetRaca.objects.filter(ptrid = vpet_raca_ptrid).first()
    tipo = PetTipo.objects.filter(pttid = vpet_tipo_pttid).first()

    Pet.objects.create(petnome = petnome, petsexo = petsexo, petcastrado = petcastrado, petdtnascto = petdtnascto, petpeso = petpeso, pet_porte_ptpid = porte, pet_raca_ptrid = raca, pet_tipo_pttid = tipo)

    #petnovo = Pet.objects.aggregate(Max('petid'))
    petidnovo = Pet.objects.order_by('-petid')[0]
    petfotosnovo = request.FILES.getlist("fotos_pet")
    if petfotosnovo:
        for foto in petfotosnovo:
            petnovo = PetFoto(pftfoto = foto, pet_petid = petidnovo)
            petnovo.save()

    # img = Image.open(petfotosnovo)
    # path = os.path.join(settings.BASE_DIR, f'media/adocao/images/pet{date.today()}-{petfotosnovo.name}')
    # img = img.save(path)
    return redirect(adocao)
    # for foto in petfotosnovo:
    #     PetFoto.objects.create(pftfoto = foto, pet_petid = petidnovo)
    # fotosnovo = PetFoto.objects.filter(pet_petid = petidnovo)
    # return render(request, "adocao.html", {"petnovo": petidnovo, "petfotosnovo": fotosnovo})
