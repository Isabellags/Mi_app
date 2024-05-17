# mi_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OrdenCompra
from django.urls import path
from . import views
from django.contrib.auth import authenticate, login
from .models import Libro

def index(request):
    libros = Libro.objects.all()
    return render(request, 'index.html', {'libros': libros})


def listar_ordenes(request):
    ordenes = OrdenCompra.objects.all()
    return render(request, 'orders.html', {'ordenes': ordenes})

def detalle_orden(request, orden_id):
    orden = get_object_or_404(OrdenCompra, pk=orden_id)
    return render(request, 'order_detail.html', {'orden': orden})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Cambia 'index' al nombre de tu vista principal
        else:
            # Si la autenticación falla, puedes mostrar un mensaje de error o redirigir a otra página
            return render(request, 'login.html', {'error_message': 'Credenciales incorrectas'})
    else:
        return render(request, 'login.html')
    
def login_view(request):
    return render(request, 'login.html')    











