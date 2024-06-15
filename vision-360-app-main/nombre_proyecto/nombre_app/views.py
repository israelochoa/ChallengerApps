
from django.shortcuts import render, redirect, get_object_or_404
from .models import Campus,Bloque
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core import serializers
from django.http import JsonResponse
import json
# Create your views here.
def index (request):
    return render (request,"pageUtils/index.html")



def homeView (request):
    #user = request.user
    print("bloques_campus_view")
    campuss = Campus.objects.filter(estado=True).distinct()
    if campuss.exists():
        campuss_serializados = serializers.serialize('json', campuss)
        campuss_data = json.loads(campuss_serializados)
    else:
        campuss_data = []
    bloques = Bloque.objects.all()
    print("bloques_campus_view")
    print(bloques)
    if (len(bloques)>0):
            bloques_serializados = serializers.serialize('json', bloques)
            bloques_data = json.loads(bloques_serializados)
    else:
            bloques_data = []
    #if user.is_superuser:
       ### contexto = {
       #     'user': user,
       #     }
       # return render(request, "RestaurantBooking/PageUtils/home-admin.html", contexto)
    ###else:
    contexto = {
         "bloques":bloques_data,
        'campus':campuss,
        'campuss': campuss_data
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


def bloques_campus_view(request, campus_id):
    # Obtener la carrera específica o devolver un error 404 si no existe
    campusList = get_object_or_404(Campus, id=campus_id)
    campuss = Campus.objects.filter(estado=True).distinct()
    
    # Filtrar los bloques asociados a la carrera
    bloques = Bloque.objects.filter(campus=campusList)
    print("bloques_campus_view")
    print(bloques)
        # ...
    if bloques.exists():
        bloques_serializados = serializers.serialize('json', bloques)
        bloques_data = json.loads(bloques_serializados)
    else:
        bloques_data = []

    contexto = {
        'campus':campuss,
        'bloques': bloques_data
    }

    return render(request, "pagesFacultades/bloques-carrera.html",contexto)

    
