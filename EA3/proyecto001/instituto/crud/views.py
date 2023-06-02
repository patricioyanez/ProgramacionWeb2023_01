from django.shortcuts import render
from .models import Marca
# Create your views here.

def marca(request):
    context = {}

    if request.method == 'POST':
        # capturar info del formulario
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST
# detecta si fue presionado el botón Grabar
        if 'Grabar' in request.POST: 
            # guardar en la base de datos
            if id == 0: # insert
                Marca.objects.create(nombre = nombre, activo=activo)
                context = {'exito': 'Datos guardados'}
            else: # update
                try:
                    item = Marca.objects.get(id = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito': 'Datos modificados'}
                except:
                    context = {'error': 'Id no encontrado'}
        if 'Listar' in request.POST: 
            context['listado'] = Marca.objects.all() # select * from marca

    return render(request, 'marca.html', context)