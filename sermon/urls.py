from django.urls import path

from .views import *

urlpatterns = [
    path('sermon/', SermonsView.as_view(), name='sermons'),
    path('sermon/<int:pk>', SermonView.as_view(), name='sermon'),
]
