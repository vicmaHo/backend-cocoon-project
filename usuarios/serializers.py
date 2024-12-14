from .models import Usuario, Arrendatario, Arrendador, Estudiante
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = ['id', 'username', 'email', 'last_name', 'first_name', 'password']



class ArrendatarioSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='usuario.user.id', read_only=True)
    username = serializers.CharField(source='usuario.user.username', read_only=True)
    tipo = serializers.CharField(source='usuario.tipo', read_only=True)
    email = serializers.EmailField(source='usuario.user.email', read_only=True)
    first_name = serializers.CharField(source='usuario.user.first_name', read_only=True)
    last_name = serializers.CharField(source='usuario.user.last_name', read_only=True)
    telefono = serializers.CharField(source='usuario.telefono', read_only=True)
    profile_picture = serializers.ImageField(source='usuario.profile_picture', read_only=True)

    class Meta:
        model = Arrendatario
        fields = [
            'id', 
            'username', 
            'tipo',
            'email', 
            'first_name', 
            'last_name', 
            'telefono',
            'profile_picture',
        ]

class EstudianteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='usuario.user.id', read_only=True)
    username = serializers.CharField(source='arrendatario.usuario.user.username', read_only=True)
    tipo = serializers.CharField(source='arrendatario.usuario.tipo', read_only=True)
    email = serializers.EmailField(source='arrendatario.usuario.user.email', read_only=True)
    first_name = serializers.CharField(source='arrendatario.usuario.user.first_name', read_only=True)
    last_name = serializers.CharField(source='arrendatario.usuario.user.last_name', read_only=True)
    telefono = serializers.CharField(source='arrendatario.usuario.telefono', read_only=True)
    profile_picture = serializers.ImageField(source='arrendatario.usuario.profile_picture', read_only=True)

    class Meta:
        model = Estudiante
        fields = [
            'id',
            'username', 
            'tipo',
            'email', 
            'first_name', 
            'last_name', 
            'telefono', 
            'constancia_universidad', 
            'universidad',
            'profile_picture',
        ]
        
class ArrendadorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='usuario.user.id', read_only=True)
    username = serializers.CharField(source='usuario.user.username', read_only=True)
    tipo = serializers.CharField(source='usuario.tipo', read_only=True)
    email = serializers.EmailField(source='usuario.user.email', read_only=True)
    first_name = serializers.CharField(source='usuario.user.first_name', read_only=True)
    last_name = serializers.CharField(source='usuario.user.last_name', read_only=True)
    telefono = serializers.CharField(source='usuario.telefono', read_only=True)
    ocupacion = serializers.CharField()
    profile_picture = serializers.ImageField(source='usuario.profile_picture', read_only=True)

    class Meta:
        model = Arrendador
        fields = [
            'id', 
            'username', 
            'tipo',
            'email', 
            'first_name', 
            'last_name', 
            'telefono', 
            'ocupacion',
            'profile_picture',
        ]