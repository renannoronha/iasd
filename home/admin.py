from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'endereco']

@admin.register(HorariosCulto)
class HorariosCultoAdmin(admin.ModelAdmin):
    list_display = ['weekday', 'time']

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ordem', 'upperText', 'subtitulo', 'ativo']
    ordering = ['ordem']