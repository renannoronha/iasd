from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ['title', 'speaker', 'date']
    ordering = ['-date']
