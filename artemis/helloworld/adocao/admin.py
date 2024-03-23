from django.contrib import admin
from .models import Pet, PetRaca, PetTipo, PetFoto, PetPorte, Pessoa
admin.site.register(Pet)
admin.site.register(PetRaca)
admin.site.register(PetTipo)
admin.site.register(PetFoto)
admin.site.register(PetPorte)
admin.site.register(Pessoa)

# Register your models here.
