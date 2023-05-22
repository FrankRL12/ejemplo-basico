from django.shortcuts import render
from .models import Galeria

# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')


def galeria(request):
    galeria=Galeria.objects.all()
    return render(request, 'galeria.html', {"galerias": galeria})
