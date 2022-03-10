from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ['name']