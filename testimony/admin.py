from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import *

# Register your models here.
class TestimonyAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Testimony
        fields = ['image', 'name', 'shortDescription', 'description', 'video']

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ['name']
    form = TestimonyAdminForm