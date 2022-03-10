from django.urls import path

from .views import *

urlpatterns = [
    path('testimony/', TestimoniesView.as_view(), name='testimonies'),
    path('testimony/<int:pk>/', TestimonyView.as_view(), name='testimony'),
]
