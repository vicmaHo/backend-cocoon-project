from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


# solicitud de cambio de contraseña
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("El email no está registrado.")
        return value


# verificacion de solicitud y cambio de contrasena
class PasswordResetSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, min_length=8)

    def validate(self, data):
        try:
            user_id = urlsafe_base64_decode(data['uid']).decode()
            user = User.objects.get(pk=user_id)
        except Exception:
            raise serializers.ValidationError("El enlace de recuperación no es válido.")
        
        if not default_token_generator.check_token(user, data['token']):
            raise serializers.ValidationError("El token es inválido o ha expirado.")
        
        return data

    def save(self):
        user_id = urlsafe_base64_decode(self.validated_data['uid']).decode()
        user = User.objects.get(pk=user_id)
        user.set_password(self.validated_data['new_password'])
        user.save()