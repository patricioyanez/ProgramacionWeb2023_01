from . import views
from django.urls import path

urlpatterns = [
    path('marca', views.marca, name='marca'),
    
]
