from .models import Resena
from rest_framework import viewsets, permissions
from .serializer import ResenaSerializer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from datetime import datetime

class ResenaViewSet(viewsets.ModelViewSet):
    queryset= Resena.objects.all()
    serializer_class = ResenaSerializer
    authentication_classes = [TokenAuthentication]  # Autenticación por token
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados
    filter_backends = [DjangoFilterBackend]  # Habilitar filtros
    filterset_fields = ['propiedad']  # Permitir filtrar por propiedad
    
    # la logica de la fecha queda en el viewset, no en el serializer, y no se manda fecha
    def perform_create(self, serializer):
        serializer.save(fecha=datetime.today())