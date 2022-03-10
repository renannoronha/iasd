from django.urls import path

from .views import *

urlpatterns = [
    path('ministry/', MinistriesView.as_view(), name='ministries'),
]
