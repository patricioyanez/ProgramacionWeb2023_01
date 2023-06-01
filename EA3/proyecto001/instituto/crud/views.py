from django.shortcuts import render
from .models import Marca
# Create your views here.

def marca(request):


    return render(request, 'marca.html')