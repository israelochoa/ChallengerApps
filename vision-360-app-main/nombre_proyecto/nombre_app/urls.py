from django.urls import path
from .views import inicio_view, login_view, homeView, bloques_campus_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', inicio_view, name="page-comenzar"),
    path('login/', login_view, name="page-login"),
    path('inicio/', homeView, name="page-home"),
    path('carrera/<int:campus_id>/bloques/', bloques_campus_view, name='bloques_campus'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)