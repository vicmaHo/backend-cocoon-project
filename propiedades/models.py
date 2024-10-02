from django.db import models
from usuarios.models import Arrendador
# usar arrendador como llave foranea

# Create your models here.
class Propiedad(models.Model):
    arrendador = models.ForeignKey(Arrendador, on_delete=models.CASCADE)  # Relación con Arrendador
    nombre = models.CharField(max_length=50, default='')
    tipo_vivienda = models.CharField(max_length=50)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=50)
    precio = models.FloatField()
    estado = models.CharField(max_length=50)
    reglas = models.TextField()
    servicios = models.TextField()
    fotos = models.CharField(max_length=100)
    videos = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tipo_vivienda} - {self.direccion}"