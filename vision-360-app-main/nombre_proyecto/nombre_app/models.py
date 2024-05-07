

from django.db import models
from django.utils import timezone

class Facultad(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=100)
    ubicacion = models.URLField(blank=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    class Meta:
        db_table = 'Facultad'
    def __str__(self):
        return self.nombre



class Campus(models.Model):
    codigo_identificativo= models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)  # Campo booleano para el estado, por defecto True (activo)
    imagen = models.ImageField(upload_to='media/bloque_campus/')  # Directorio donde se guardarán las imágenes
    class Meta:
        db_table = 'Campus'
    def __str__(self):
        return self.nombre
    
class Bloque(models.Model):
    codigo_identificativo= models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)  # Campo booleano para el estado, por defecto True (activo)
    imagen = models.ImageField(upload_to='media/bloque_fotos/')  # Directorio donde se guardarán las imágenes
    link = models.URLField(blank=True)  # Campo para el enlace, puede estar vacío
    latitud=models.FloatField(default=0.0, null=False)
    longitud=models.FloatField(default=0.0, null=False)
    class Meta:
            db_table = 'Bloque'
    def __str__(self):
        return self.nombre

