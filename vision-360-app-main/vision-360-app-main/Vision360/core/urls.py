from django.urls import path
from .views import homeView, login_view, logout_view, inicio_view,  lista_facultades, lista_campuss, registrar_campus, registrar_facultad, listar_bloques, registrar_bloque, bloques_campus
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('inicio/', homeView, name="page-home"),
    path('', inicio_view, name="page-comenzar"),
    path('login/', login_view, name="page-login"),
    path('logout/', logout_view, name='page-logout'),
    path('facultades/', lista_facultades, name='page-facultades'),
    path('carreras/', lista_campuss, name='page-carreras'),
    path('bloques/', listar_bloques, name='page-bloques'),
    path('nueva-carrera/', registrar_campus, name="registrar-carrera"),
    path('nueva-facultad/', registrar_facultad, name="registrar-facultad"),
    path('nuevo-bloque/', registrar_campus, name="registrar-bloque"),


    
    path('carrera/<int:carrera_id>/bloques/', bloques_campus, name='bloques_campus'),





   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)