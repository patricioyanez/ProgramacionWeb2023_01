from django.shortcuts import render
from .models import Marca, Categoria, Genero
# Create your views here.
# importar Forms de django
from .forms import ClienteForm

def clienteForm(request):
    context = {'form': ClienteForm()}
    if request.method == 'POST':
        if 'Grabar' in request.POST:
            form = ClienteForm(request.POST)
            if form.is_valid():
                form.save()
                context['exito'] = 'Los datos fueron guardados'
            else:
                context['error'] = 'Los datos no fueron guardados'
    

    return render(request, 'clienteForm.html', context)

def categoria(request):
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
                Categoria.objects.create(nombre = nombre, activo=activo)
                context = {'exito': 'Datos guardados'}
            else: # update
                try:
                    item = Categoria.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito': 'Datos modificados'}
                except:
                    context = {'error': 'Id no encontrado'}
        elif 'Listar' in request.POST: 
            context['listado'] = Categoria.objects.all() # select * from categoria
        elif 'Buscar' in request.POST:
            try:
                item = Categoria.objects.get(pk = id)
                context = {'item': item}
            except:
                context = {'error': 'Id no encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = Categoria.objects.get(pk = id)
                item.delete()
                context = {'exito': 'Valor eliminado'}
            except:
                context = {'error': 'Id no encontrado'}
            
    return render(request, 'categoria.html', context)

def genero(request):
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
                Genero.objects.create(nombre = nombre, activo=activo)
                context = {'exito': 'Datos guardados'}
            else: # update
                try:
                    item = Genero.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito': 'Datos modificados'}
                except:
                    context = {'error': 'Id no encontrado'}
        elif 'Listar' in request.POST: 
            context['listado'] = Genero.objects.all() # select * from categoria
        elif 'Buscar' in request.POST:
            try:
                item = Genero.objects.get(pk = id)
                context = {'item': item}
            except:
                context = {'error': 'Id no encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = Genero.objects.get(pk = id)
                item.delete()
                context = {'exito': 'Valor eliminado'}
            except:
                context = {'error': 'Id no encontrado'}
            
    return render(request, 'genero.html', context)

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
                    item = Marca.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito': 'Datos modificados'}
                except:
                    context = {'error': 'Id no encontrado'}
        elif 'Listar' in request.POST: 
            context['listado'] = Marca.objects.all() # select * from marca
        elif 'Buscar' in request.POST:
            try:
                item = Marca.objects.get(pk = id)
                context = {'item': item}
            except:
                context = {'error': 'Id no encontrado'}
        elif 'Eliminar' in request.POST:
            try:
                item = Marca.objects.get(pk = id)
                item.delete()
                context = {'exito': 'Valor eliminado'}
            except:
                context = {'error': 'Id no encontrado'}
            
    return render(request, 'marca.html', context)
    ## Ejercicio: CREAR CRUD para GENERO