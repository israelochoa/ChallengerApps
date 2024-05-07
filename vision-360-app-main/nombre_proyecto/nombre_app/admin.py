from django.contrib import admin

from .models import Facultad,Bloque, Campus
# Register your models here.

admin.site.register(Facultad)
admin.site.register(Campus)
admin.site.register(Bloque)
