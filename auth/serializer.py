from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


# serializadores para register y login (solo para documentación)
class RegisterSchemaSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        help_text="Nombre de usuario único."
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Contraseña para el usuario."
    )
    first_name = serializers.CharField(
        required=True,
        max_length=50,
        help_text="Nombre del usuario."
    )
    last_name = serializers.CharField(
        required=True,
        max_length=50,
        help_text="Apellido del usuario."
    )
    email = serializers.EmailField(
        required=True,
        help_text="Correo electrónico único."
    )
    telefono = serializers.CharField(
        required=True,
        max_length=15,
        help_text="Número de teléfono del usuario."
    )
    is_arrendador = serializers.BooleanField(
        required=True,
        help_text="Indica si el usuario es arrendador."
    )
    ocupacion = serializers.CharField(
        required=True,
        max_length=100,
        help_text="Ocupación actual del usuario."
    )
    is_estudiante = serializers.BooleanField(
        required=True,
        help_text="Indica si el usuario es estudiante."
    )
    constancia_universidad = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        help_text="Enlace al archivo de constancia universitaria (opcional)."
    )
    universidad = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        help_text="Nombre de la universidad del usuario (opcional)."
    )
    profile_picture = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        help_text="Enlace a la imagen de perfil del usuario (opcional)."
    )
class LoginSchemaSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, help_text="Nombre de usuario")
    password = serializers.CharField(write_only=True, required=True, help_text="Contraseña")

class DatosUsuarioSerializer(serializers.Serializer):
    id = serializers.IntegerField(help_text="ID único del usuario.")
    username = serializers.CharField(help_text="Nombre de usuario.")
    tipo = serializers.CharField(help_text="Tipo de usuario, por ejemplo: arrendatario.")
    email = serializers.EmailField(help_text="Correo electrónico del usuario.")
    first_name = serializers.CharField(help_text="Nombre del usuario.")
    last_name = serializers.CharField(help_text="Apellido del usuario.")
    telefono = serializers.CharField(help_text="Número de teléfono del usuario.")
    profile_picture = serializers.URLField(
        help_text="URL de la imagen de perfil del usuario."
    )

class RegisterResponseSerializer(serializers.Serializer):
    token = serializers.CharField(help_text="Token de autenticación generado para el usuario.")
    tipo = serializers.CharField(help_text="Tipo de usuario, por ejemplo: arrendatario.")
    created = serializers.BooleanField(help_text="Indica si el usuario fue creado exitosamente.")
    datos = DatosUsuarioSerializer(help_text="Información detallada del usuario registrado.")



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