from .models import Reserva
from rest_framework import viewsets, permissions
from .serializer import ReservaSerializer
from django.db import transaction

from django.core.mail import send_mail
from django.conf import settings

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ReservaViewSet(viewsets.ModelViewSet):
    queryset= Reserva.objects.all()
    serializer_class = ReservaSerializer
    authentication_classes = [TokenAuthentication]  # Autenticación por token
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados
    
    def perform_create(self, serializer):
        with transaction.atomic():
                reserva = serializer.save()
                propiedad = reserva.propiedad
                if propiedad.estado == "disponible":
                    propiedad.estado = "en proceso de reserva"
                    propiedad.save()
                else:
                    raise Exception("La propiedad no está disponible para reservar.")
        # Enviar correo al arrendador
        arrendador = propiedad.arrendador
        mensaje = (
            f"Hola {arrendador.usuario.user.first_name} {arrendador.usuario.user.last_name},\n\n"
            f"Se ha realizado una nueva reserva para tu propiedad: {propiedad.nombre}.\n\n"
            f"Comunícate con el arrendatario interesado para llevar a cabo el proceso de reserva.\n\n"
            f"Detalles de la reserva:\n"
            f"- Arrendatario: {reserva.arrendatario.usuario.user.first_name} {reserva.arrendatario.usuario.user.last_name}\n"
            f"- Correo del arrendatario: {reserva.arrendatario.usuario.user.email}\n"
            f"- Telefono del arrendatario: {reserva.arrendatario.usuario.telefono}\n"
            f"- Fecha de inicio: {reserva.fecha_inicio}\n"
            f"- Fecha de fin: {reserva.fecha_final}\n\n"
            "Saludos,\nCoccon Home Team."
        )
        send_mail(
            subject="Nueva reserva realizada",
            message=mensaje,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[arrendador.usuario.user.email],  # Correo del arrendador
            fail_silently=False,
        )