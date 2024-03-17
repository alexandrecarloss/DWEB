from django.shortcuts import render

from .forms import LocationForm
from .models import City

def index(request):
    form = LocationForm()
    return render(request, 'index.html', {'form':form})

def load_cities(request):
    country_id = request.GET.get("country")
    cities = City.objects.filter(country_id=country_id)
    return render(request, "city_options.html", {"cities": cities})
# Create your views here.
