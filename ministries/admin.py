from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ['title']