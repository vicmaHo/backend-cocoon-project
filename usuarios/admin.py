from django.contrib import admin
from .models import Usuario, Arrendatario, Arrendador
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Arrendatario)
admin.site.register(Arrendador)
