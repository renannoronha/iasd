from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(template_name='home/base.html'), name='home'),
]
