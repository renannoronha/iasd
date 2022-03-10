from django.urls import path

from .views import *

urlpatterns = [
    path('newsletter/', NewsView.as_view(), name='news'),
    path('newsletter/<int:pk>/', NewsletterView.as_view(), name='newsletter'),
]
