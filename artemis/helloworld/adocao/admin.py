from django.contrib import admin
from .models import Pet, PetRaca, PetTipo, PetFoto, PetPorte
admin.site.register(Pet)
admin.site.register(PetRaca)
admin.site.register(PetTipo)
admin.site.register(PetFoto)
admin.site.register(PetPorte)

# Register your models here.
