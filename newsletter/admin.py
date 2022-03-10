from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import *

# Register your models here.
class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = ['image', 'date', 'title', 'shortDescription', 'text', 'videoLink']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['date', 'title']
    form = NewsAdminForm