from django.shortcuts import render
from .models import Marca
# Create your views here.

def marca(request):
    context = {}
    context['listado'] = Marca.objects.all() # select * from marca

    return render(request, 'marca.html', context)