from .models import Reserva
from rest_framework import viewsets, permissions
from .serializer import ReservaSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ReservaViewSet(viewsets.ModelViewSet):
    queryset= Reserva.objects.all()
    serializer_class = ReservaSerializer
    authentication_classes = [TokenAuthentication]  # Autenticación por token
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados