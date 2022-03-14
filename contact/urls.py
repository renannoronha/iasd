from django.urls import path

from .views import *

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('donate/', DonateView.as_view(), name='donate'),
]
