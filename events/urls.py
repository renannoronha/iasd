from django.urls import path

from .views import *

urlpatterns = [
    path('events/', EventsView.as_view(), name='events'),
    path('events/<int:pk>/', EventView.as_view(), name='event'),
]
