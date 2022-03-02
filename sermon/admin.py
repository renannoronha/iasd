from django.contrib import admin
from django.contrib import messages
from django_object_actions import DjangoObjectActions
from .models import *

from .views import getNewVideos

# Register your models here.
@admin.register(Sermon)
class SermonAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ['title', 'speaker', 'date', 'ativo']
    ordering = ['-date']
    
    def importar_videos_novos(modeladmin, request, queryset):
        try:
            getNewVideos()
            messages.success(request, "Lista de Vídeos atualizada com sucesso!")
        except Exception as e:
            messages.error(request, "Erro ao buscar os vídeos no Youtube.")

    importar_videos_novos.label = "Impotar Vídeos Novos"
    importar_videos_novos.short_description = "Puxar vídeos novos do Youtube automaticamente"

    changelist_actions = ('importar_videos_novos', )
