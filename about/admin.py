from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(AboutPrimeiraSecao)
class AboutPrimeiraSecaoAdmin(admin.ModelAdmin):
    list_display = ['titulo1', 'titulo2', 'titulo3', 'servicesTitulo']

@admin.register(AboutSegundaSecao)
class AboutSegundaSecaoAdmin(admin.ModelAdmin):
    list_display = ['upperText', 'titulo']

@admin.register(AboutTerceiraSecao)
class AboutTerceiraSecaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'dado1', 'dado2', 'dado3']

@admin.register(Pastor)
class PastorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo']