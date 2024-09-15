from .models import Propiedad
from rest_framework import viewsets, permissions
from .serializer import PropiedadSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class PropiedadViewSet(viewsets.ModelViewSet):
    queryset= Propiedad.objects.all()
    serializer_class = PropiedadSerializer
    authentication_classes = [TokenAuthentication]  # Autenticación por token
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados