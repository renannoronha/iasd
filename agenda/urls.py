from django.urls import path

from .views import *

urlpatterns = [
    path('agenda/', AgendaView.as_view(), name='agenda'),
]
