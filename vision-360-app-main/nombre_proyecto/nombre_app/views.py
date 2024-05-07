
from django.shortcuts import render, redirect, get_object_or_404
from .models import Campus,Bloque
# Create your views here.
def inicio_view (request):
    return render (request,"pageUtils/inicio.html")


def homeView (request):
    #user = request.user
    campuss = Campus.objects.filter(estado=True).distinct()
    
    #if user.is_superuser:
       ### contexto = {
       #     'user': user,
       #     }
       # return render(request, "RestaurantBooking/PageUtils/home-admin.html", contexto)
    ###else:
    contexto = {
        'campuss': campuss
        }
    print("--------------------------------------contexto---------------------------------");
    print(contexto);
    return render(request, "pageUtils/home-user.html",contexto)
    
def login_view(request):
    #if request.method == 'POST':
      #  username = request.POST['username']
      #  password = request.POST['password']

      #  user = authenticate(request, username=username, password=password)

      #  if user is not None:
      ##      login(request, user)
      #3      return redirect('page-home')
        ###else:
      #      error_message = 'Existe un error las con crendenciales.'
      #      return render(request, 'RestaurantBooking/PageUtils/login.html', {'error_message': error_message})
    #else:
       # return render(request, 'RestaurantBooking/PageUtils/login.html')
      return render(request, "pageUtils/home-user.html")

from django.core import serializers
from django.http import JsonResponse
import json

def bloques_campus_view(request, campus_id):
    # Obtener la carrera específica o devolver un error 404 si no existe
    campus = get_object_or_404(Campus, id=campus_id)
    campuss = Campus.objects.filter(estado=True).distinct()
    
    # Filtrar los bloques asociados a la carrera
    bloques = Bloque.objects.filter(campus=campus)
    

        # ...
    if bloques.exists():
        bloques_serializados = serializers.serialize('json', bloques)
        bloques_data = json.loads(bloques_serializados)
    else:
        bloques_data = []

    contexto = {
        'campus': campus.nombre,
        'bloques': bloques_data,
        'campuss': list(campuss.values('nombre', 'id','codigo_identificativo')),
    }

    return render(request, "pagesFacultades/bloques-carrera.html",contexto)

    
