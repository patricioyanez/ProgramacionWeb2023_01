from django.contrib import admin
from .models import Marca, Categoria, Cliente,Genero
# Register your models here.

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Genero)