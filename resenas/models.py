from django.db import models

# Create your models here.
class Resena(models.Model):
    calificacion = models.IntegerField()
    comentario = models.TextField()
    propiedad = models.ForeignKey('propiedades.Propiedad', on_delete=models.CASCADE)
    arrendatario = models.ForeignKey('usuarios.Arrendatario', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.pk} - {self.propiedad} - {self.arrendatario}"