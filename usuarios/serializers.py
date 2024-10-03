from .models import Usuario, Arrendatario, Arrendador, Estudiante
from rest_framework import serializers
from django.contrib.auth.models import User

# Mediante anidacion de serializers
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name']

# class UsuarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'telefono']
        
# class ArrendatarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Arrendatario
#         fields = '__all__'

# class ArrendadorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Arrendador
#         fields = '__all__'

# class EstudianteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Estudiante
#         fields = '__all__'


# Sin anidacion de serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = ['id', 'username', 'email', 'password', 'last_name', 'first_name']


class ArrendatarioSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='usuario.user.id', read_only=True)
    username = serializers.CharField(source='usuario.user.username', read_only=True)
    email = serializers.EmailField(source='usuario.user.email', read_only=True)
    first_name = serializers.CharField(source='usuario.user.first_name', read_only=True)
    last_name = serializers.CharField(source='usuario.user.last_name', read_only=True)
    telefono = serializers.CharField(source='usuario.telefono', read_only=True)

    class Meta:
        model = Arrendatario
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'telefono'
        ]

class EstudianteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='usuario.user.id', read_only=True)
    username = serializers.CharField(source='arrendatario.usuario.user.username', read_only=True)
    email = serializers.EmailField(source='arrendatario.usuario.user.email', read_only=True)
    first_name = serializers.CharField(source='arrendatario.usuario.user.first_name', read_only=True)
    last_name = serializers.CharField(source='arrendatario.usuario.user.last_name', read_only=True)
    telefono = serializers.CharField(source='arrendatario.usuario.telefono', read_only=True)

    class Meta:
        model = Estudiante
        fields = [
            'id',
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'telefono', 
            'constancia_universidad', 
            'universidad'
        ]
        
class ArrendadorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='usuario.user.id', read_only=True)
    username = serializers.CharField(source='usuario.user.username', read_only=True)
    email = serializers.EmailField(source='usuario.user.email', read_only=True)
    first_name = serializers.CharField(source='usuario.user.first_name', read_only=True)
    last_name = serializers.CharField(source='usuario.user.last_name', read_only=True)
    telefono = serializers.CharField(source='usuario.telefono', read_only=True)
    ocupacion = serializers.CharField()
    password = serializers.CharField(source='usuario.user.password', read_only=True)

    class Meta:
        model = Arrendador
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'telefono', 
            'ocupacion',
            'password'
        ]