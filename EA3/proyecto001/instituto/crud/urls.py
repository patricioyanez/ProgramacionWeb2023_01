from . import views
from django.urls import path

urlpatterns = [
    path('marca', views.marca, name='marca'),
    path('categoria', views.categoria, name='categoria'),
    path('genero', views.genero, name='genero'),
    path('cliente', views.clienteForm, name='cliente'),
    path('menu', views.menu, name='menu'),
    
]
# 127.0.0.1:8000/crud/marca
# 127.0.0.1:8000/crud/genero

# Ejercicio: Definir el modelo Producto, migrarlo y 
# crear para este modelo el Django Forms. Incluirlo en el menú