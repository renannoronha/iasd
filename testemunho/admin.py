from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Testemunho)
class TestemunhoAdmin(admin.ModelAdmin):
    list_display = ['name']