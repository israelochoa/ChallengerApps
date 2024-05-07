from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.views.generic import DetailView, View
from datetime import date
from django.contrib import messages
from .models import Facultad, Campus, Bloque
from .forms import CampusForm, FacultadForm, BloqueForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import permission_required

 


def homeView (request):
    user = request.user
    campuss = Campus.objects.filter(estado=True).distinct()
    

    contexto = {
        'campuss': campuss,
        }
    print("-------------------------contexto-------------\  ")
    print(contexto)
    return render(request, "RestaurantBooking/PageUtils/home-user.html",contexto)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('page-home')
        else:
            error_message = 'Existe un error las con crendenciales.'
            return render(request, 'RestaurantBooking/PageUtils/login.html', {'error_message': error_message})
    else:
        return render(request, 'RestaurantBooking/PageUtils/login.html')

def logout_view(request):
    logout(request)
    # Redirecciona a la página de inicio o a donde desees después de cerrar sesión
    return redirect('page-login')

@permission_required('auth.is_superuser')
def lista_facultades(request):
    facultades = Facultad.objects.all()
    return render(request, 'RestaurantBooking/PagesFacultades/facultades.html', {'facultades': facultades})

@permission_required('auth.is_superuser')
def registrar_facultad(request):
    if request.method == 'POST':
        form = FacultadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-facultades')  # Reemplaza 'nombre_de_la_url' con el nombre de la URL de la página de inicio
    else:
        form = FacultadForm()
    return render(request, 'RestaurantBooking/PagesFacultades/nueva-facultad.html', {'form': form})

@permission_required('auth.is_superuser')
def lista_campuss(request):
    campuss = Campus.objects.all()
    return render(request, 'RestaurantBooking/PagesFacultades/carreras.html', {'campuss': campuss})

@permission_required('auth.is_superuser')
def registrar_campus(request):
    if request.method == 'POST':
        form = CampusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-carreras')  # Reemplaza 'nombre_de_la_url' con el nombre de la URL de la página de inicio
    else:
        form = CampusForm()
    return render(request, 'RestaurantBooking/PagesFacultades/nueva-carrera.html', {'form': form})

@permission_required('auth.is_superuser')
def listar_bloques(request):
    bloques = Bloque.objects.all()
    return render(request, 'RestaurantBooking/PagesFacultades/bloques.html', {'bloques': bloques})

@permission_required('auth.is_superuser')
def registrar_bloque(request):
    if request.method == 'POST':
        form = BloqueForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('page-bloques')  # Redirige a la página de lista de bloques
    else:
        form = BloqueForm()
    return render(request, 'RestaurantBooking/PagesFacultades/nuevo-bloque.html', {'form': form})


def bloques_campus(request, campus_id):
    # Obtener la carrera específica o devolver un error 404 si no existe
    campus = get_object_or_404(Campus, id=campus_id)
    campuss = Campus.objects.filter(estado=True).distinct()
    
    # Filtrar los bloques asociados a la carrera
    bloques = Bloque.objects.filter(campus=campus)
    
       
    contexto = {
        'campus': campus,
        'bloques': bloques,
        'campuss': campuss,
    }
    return render(request, "RestaurantBooking/PagesFacultades/bloques-carrera.html", contexto)


def inicio_view (request):
    return render (request,"RestaurantBooking/PageUtils/inicio.html")