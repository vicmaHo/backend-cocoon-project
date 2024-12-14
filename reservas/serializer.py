from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        
        # validar el estado de la propiedad para proceder con la reserva
        def validate(self, data):
            propiedad = data.get('propiedad')
            if propiedad.estado != "disponible":
                raise serializers.ValidationError("La propiedad no está disponible para reservar.")
            return data
        
