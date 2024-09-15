from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Usuario(models.Model):
    # Hare uso del usuario predefinido por Django, extendiendo sus atributos por defecto y agregando el telefono
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # nombre = models.CharField(max_length=50)
    # correo = models.EmailField(max_length=50, unique=True)
    # contrasena = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.user.id} - { self.user.username}"

class Arrendador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    ocupacion = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.usuario.user.id} - {self.usuario.user.username} - {self.ocupacion}"
    

class Arrendatario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.usuario.user.username
    
class Estudiante(models.Model):
    arrendatario = models.OneToOneField(Arrendatario, on_delete=models.CASCADE, primary_key=True)
    constancia_universidad = models.CharField(max_length=100)
    universidad = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.arrendatario.usuario.user.username} - {self.universidad}"

    