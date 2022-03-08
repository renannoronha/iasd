from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['departamento']

@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ['data', 'departamento', 'nome']
    list_filter = ['data', 'departamento']
