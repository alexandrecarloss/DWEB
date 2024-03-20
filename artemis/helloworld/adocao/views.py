from django.shortcuts import render
# from django.http import HttpResponse
#from .models import Pet, PetRaca, PetTipo
#from .forms import especieForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def adocao(request):
    #form = especieForm()
    return render(request, 'adocao.html')
    #return render(request, 'adocao.html', {'form':form})
    # pettipos = PetTipo.objects.all()
    # pets = Pet.objects.all()
    #petracas = PetRaca.objects.all().select_related
    #searchTipo = request.GET.get('especie')('pet_tipo_pttid')
    #return render(request, 'adocao.html', {'pets': pets, 'pettipos': pettipos, 'form': form})

# def load_racas(request):
#     id_specie = request.GET.get('especie')
#     racas = PetRaca.objects.filter(pet_tipo_pttid = id_specie)
#     return render(request, "raca_options.html", {"racas": racas})

# Create your views here.
