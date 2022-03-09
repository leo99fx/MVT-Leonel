from django.urls import path
from .views import inicio, plantilla
from django.urls import path, include

urlpatterns = [
    path('', inicio),
    path('plantilla/', plantilla),
]