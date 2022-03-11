from django.urls import path

from .views import *

urlpatterns = [
    path('gallery/', GalleryView.as_view(), name='gallery'),
]
