from django.shortcuts import render, redirect
from .models import Pet, PetRaca, PetTipo, PetFoto, Pessoa, PetPorte, PetAdocao, Ong
from django.views import View
from django.conf import settings
from datetime import date
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib import messages
from helloworld.context_processors import *
from accounts.views import cadastro_dados 

def index(request):
    return render(request, 'index.html')

def adocao(request):
    nomePesquisa = request.GET.get('nomepesquisa')
    especie = request.GET.get('especie')
    raca = request.GET.get('raca')
    pettipos = PetTipo.objects.all()
    pessoas = Pessoa.objects.all()
    if nomePesquisa:
        pets = Pet.objects.filter(petnome__icontains=nomePesquisa).filter(petadocoes__isnull=False)
    elif especie:
        if raca:
            pets = Pet.objects.filter(pet_raca_ptrid = raca, petadocoes__isnull=False)
        else:
            pets = Pet.objects.filter(pet_tipo_pttid = especie, petadocoes__isnull=False)
    else:
        pets = Pet.objects.filter(petadocoes__isnull=False)
    pftfotos = PetFoto.objects.all()
    return render(request, 'adocao.html', {'pets': pets, 'pettipos': pettipos, 'pftfotos': pftfotos, "pessoas": pessoas, "especie": especie, "raca": raca, "nomePesquisa": nomePesquisa})

def load_racas(request):
    id_specie = request.GET.get('especie')
    racas = PetRaca.objects.filter(pet_tipo_pttid = id_specie)
    return render(request, "raca_options.html", {"racas": racas, "id_specie": id_specie})

def load_pets(request):
    especie = request.GET.get('especie')
    raca = request.GET.get('raca')  
    if raca:
        pets = Pet.objects.filter(pet_raca_ptrid = raca, petadocoes__isnull=False)
    elif especie:
        pets = Pet.objects.filter(pet_tipo_pttid = especie, petadocoes__isnull=False)
    else:
        pets = Pet.objects.all().filter(petadocoes__isnull=False)
    pftfotos = PetFoto.objects.all()
    return render(request, "load_pets.html", {"pets": pets, "raca": raca, "pftfotos": pftfotos, "especie": especie})

@login_required(login_url="/accounts/login")
def petdetalhe(request, petid):
    pet = Pet.objects.filter(petid = petid).first()
    today = date.today()
    petidade = today.year - pet.petdtnascto.year - ((today.month, today.day) < (pet.petdtnascto.month, pet.petdtnascto.day))
    pftfotos = PetFoto.objects.filter(pet_petid = pet.petid)
    if petidade < 1:
        if pet.petdtnascto.month > today.month:
            petmes = 12 - pet.petdtnascto.month + today.month - (today.day < pet.petdtnascto.day)
        else:
            petmes = today.month - pet.petdtnascto.month - (today.day < pet.petdtnascto.day)
        return render(request, "pagDetalheAdocao.html", {"pet": pet, "petid": petid, "pftfotos": pftfotos, "petmes": petmes})
    return render(request, "pagDetalheAdocao.html", {"pet": pet, "petid": petid, "pftfotos": pftfotos, "petidade": petidade})
    
class fotopet(View):
    def get(self, request, petid, multiplo):
        pet = Pet.objects.filter(petid = petid).first()
        if multiplo == 0 or multiplo == 2:
            pftfoto = PetFoto.objects.filter(pet_petid = pet.petid).first()   
        else:
            pftfoto = PetFoto.objects.filter(pet_petid = pet.petid)
            if len(pftfoto) > 1:
                pftfotoprimeira = PetFoto.objects.filter(pet_petid = pet.petid).first()
                varias = 1
                return render(request, "load_foto_pet.html", {"pet": pet, "petid": petid, "pftfoto": pftfoto, "multiplo": multiplo, "varias": varias, "pftfotoprimeira": pftfotoprimeira})
        return render(request, "load_foto_pet.html", {"pet": pet, "petid": petid, "pftfoto": pftfoto, "multiplo": multiplo})

@login_required(login_url="/accounts/login")
def cadastropet(request):
    contexto = context_grupo_usuario(request)
    if contexto['dado_usuario'] == None:
        messages.error(request, 'Termine seu cadastro')
        return redirect(cadastro_dados)
    if str(request.user.groups.first()) != 'Ong':
        messages.error(request, 'Tipo de usuário não autorizado para cadastrar pets para adoção!')
        return redirect(index)
    pettipos = PetTipo.objects.all()
    petportes = PetPorte.objects.all()
    return render(request, "pagCadastroPetAdocao.html", {"pettipos": pettipos, "petportes": petportes})

def salvarpet(request):
    cursor = connection.cursor()
    petnome = request.POST.get('petnome')
    petsexo = request.POST.get('petsexo')
    petcastrado = request.POST.get('petcastrado')
    petdtnascto = request.POST.get('petdtnascto')
    petpeso = request.POST.get('petpeso')
    #FK número
    vpet_porte_ptpid = request.POST.get('petporte')
    vpet_raca_ptrid = request.POST.get('petraca')
    vpet_tipo_pttid = request.POST.get('especie')
    #FK objeto
    porte = PetPorte.objects.filter(ptpid = vpet_porte_ptpid).first()
    raca = PetRaca.objects.filter(ptrid = vpet_raca_ptrid).first()
    tipo = PetTipo.objects.filter(pttid = vpet_tipo_pttid).first()

    if str(request.user.groups.all()[0]) == 'Pessoa':
        pessoa_pesid = Pessoa.objects.filter(pesemail = request.user.email).first().pesid
        try:
            cursor.execute('call sp_inserepet (%(nome)s, %(sexo)s, %(castrado)s, %(dtnascto)s, %(peso)s, %(pessoa)s, %(porte)s, %(raca)s, %(tipo)s)', {'nome': petnome, 'sexo': petsexo, 'castrado': petcastrado, 'dtnascto': petdtnascto, 'peso': petpeso, 'pessoa': pessoa_pesid, 'porte': vpet_porte_ptpid, 'raca': vpet_raca_ptrid, 'tipo': vpet_tipo_pttid})
        except Exception as erro:
            print(erro)
            messages.error(request, 'Erro ao cadastrar pet!')
            return redirect(cadastropet)
        finally:
            cursor.close()
    elif str(request.user.groups.all()[0]) == 'Ong':
        try:
            ong = Ong.objects.filter(ongemail = request.user.email).first()
            print(ong)
            Pet.objects.create(petnome = petnome, petsexo = petsexo, petcastrado = petcastrado, petdtnascto = petdtnascto, petpeso = petpeso, pet_porte_ptpid = porte, pet_raca_ptrid = raca, pet_tipo_pttid = tipo)
            idpet = Pet.objects.order_by('-petid')[0]
            PetAdocao.objects.create(ong_ongid = ong, pet_petid = idpet)
        except Exception as erro:
            print(erro)
            messages.error(request, 'Erro ao cadastrar pet!')
            return redirect(cadastropet)   
    else:
        messages.error(request, 'Erro ao cadastrar pet!')
        return redirect(cadastropet)

    #petnovo = Pet.objects.aggregate(Max('petid'))
    petidnovo = Pet.objects.order_by('-petid')[0]
    petfotosnovo = request.FILES.getlist("fotos_pet")
    if petfotosnovo:
        for foto in petfotosnovo:
            petnovo = PetFoto(pftfoto = foto, pet_petid = petidnovo)
            petnovo.save()
    messages.success(request, 'Pet cadastrado com sucesso!')    
    return redirect(index)

def modalpet(request, petid):
    pettipos = PetTipo.objects.all()
    petportes = PetPorte.objects.all()
    pet = Pet.objects.filter(petid = petid).first()
    petfoto = PetFoto.objects.filter(pet_petid = petid).first()
    return render(request, "modalpet.html", {"pet": pet, "petfoto": petfoto, "pettipos": pettipos, "petportes": petportes})

def atualizarpet(request, petid):
    cursor = connection.cursor()
    petnome = request.POST.get('petnome')
    petsexo = request.POST.get('petsexo')
    petcastrado = request.POST.get('petcastrado')
    petdtnascto = request.POST.get('petdtnascto')
    petpeso = request.POST.get('petpeso')
    pessoa_pesid = Pessoa.objects.filter(pesemail = request.user.email).first().pesid
    vpet_porte_ptpid = request.POST.get('petporte')
    vpet_raca_ptrid = request.POST.get('petraca')
    vpet_tipo_pttid = request.POST.get('especie')
    pet = Pet.objects.filter(petid = petid).first()
    try:
        cursor.execute('call sp_alterapet (%(nome)s, %(sexo)s, %(castrado)s, %(dtnascto)s, %(peso)s, %(pessoa)s, %(porte)s, %(raca)s, %(tipo)s, %(cod)s)', {'nome': petnome, 'sexo': petsexo, 'castrado': petcastrado, 'dtnascto': petdtnascto, 'peso': petpeso, 'pessoa': pessoa_pesid, 'porte': vpet_porte_ptpid, 'raca': vpet_raca_ptrid, 'tipo': vpet_tipo_pttid, 'cod': petid})
        print(cursor)
    finally:
        cursor.close()
    # Removendo fotos antigas
    petfotoantigas = PetFoto.objects.filter(pet_petid_id = petid)
    for foto in petfotoantigas:
        foto.delete()
    petfotosnovo = request.FILES.getlist("fotos_pet")
    if petfotosnovo:
        for foto in petfotosnovo:
            petnovo = PetFoto(pftfoto = foto, pet_petid = pet)
            petnovo.save()
    messages.success(request, 'Pet atualizado com sucesso!')
    return redirect(adocao)

def removerpet(request, petid):
    pet = Pet.objects.filter(petid = petid).first()
    # Removendo fotos antigas
    try:
        petfotoantigas = PetFoto.objects.filter(pet_petid_id = petid)
        for foto in petfotoantigas:
            foto.pftfoto.delete()
            foto.delete()
        pet.delete()
        messages.success(request, 'Pet removido com sucesso!')
    except Exception as erro:
        print(erro)
        messages.error(request, 'Erro ao remover pet!')
    return redirect(adocao)