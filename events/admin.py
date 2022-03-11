from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import *

# Register your models here.
class EventsAdminForm(forms.ModelForm):
    details = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Events
        fields = ['image', 'title', 'startTime', 'endTime', 'locationName', 'locationUrl', 'address', 'details']

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'startTime', 'endTime', 'locationName']
    form = EventsAdminForm