from django.urls import path

from .views import *

urlpatterns = [
    path('escala/', EscalaView.as_view(), name='escala'),
    path('escala/eventos/', EventosView.as_view()),
]
