from django.urls import path

from .views import *

urlpatterns = [
    path('sermon/', SermonView.as_view(), name='sermon'),
]
