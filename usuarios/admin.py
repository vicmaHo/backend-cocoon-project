from django.contrib import admin
from .models import Usuario, Arrendatario, Arrendador, Estudiante
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Arrendatario)
admin.site.register(Arrendador)
admin.site.register(Estudiante)