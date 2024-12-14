from django.db import models
from propiedades.models import Propiedad
from usuarios.models import Arrendatario
# Create your models here.


class Reserva(models.Model):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    propiedad = models.ForeignKey('propiedades.Propiedad', on_delete=models.CASCADE)
    arrendatario = models.ForeignKey('usuarios.Arrendatario', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.propiedad} - {self.arrendatario}"