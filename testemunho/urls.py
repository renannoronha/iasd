from django.urls import path

from .views import *

urlpatterns = [
    path('testemunho/', TestemunhosView.as_view(), name='testemunhos'),
    path('testemunho/<int:pk>/', TestemunhoView.as_view(), name='testemunho'),
]
