from rest_framework import serializers
from .models import Resena

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'
        read_only_fields = ['fecha'] # la fecha solo se enviara en las peticiones get, no es requerida en las post
        
