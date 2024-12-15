from .models import Propiedad
from rest_framework import viewsets, permissions
from .serializer import PropiedadSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from drf_spectacular.utils import extend_schema_view, extend_schema
@extend_schema_view(
    list=extend_schema(
        summary="Listar Propiedades",
        description="Obtiene una lista de todas las propiedades existentes en la base de datos de Cocoon-Home.",
        tags=["Propiedades"]),
    retrieve=extend_schema(
        summary="Detalles de Propiedad",
        description="Obtiene los detalles de una propiedad específica por su ID.",
        tags=["Propiedades"]),
    create=extend_schema(
        summary="Crear Propiedad",
        description="Crea una nueva propiedad en la base de datos de Cocoon-Home.",
        tags=["Propiedades"]),
    update=extend_schema(
        summary="Actualizar Propiedad",
        description="Actualiza los detalles de una propiedad existente en la base de datos de Cocoon-Home.",
        tags=["Propiedades"]),
    destroy=extend_schema(
        summary="Eliminar Propiedad",
        description="Elimina una propiedad específica de la base de datos de Cocoon-Home.",
        tags=["Propiedades"]),
    partial_update=extend_schema(
        summary="Actualizar Parcialmente Propiedad",
        description="Actualiza parcialmente los detalles de una propiedad existente en la base de datos de Cocoon-Home.",
        tags=["Propiedades"]),
)

class PropiedadViewSet(viewsets.ModelViewSet):
    queryset= Propiedad.objects.all()
    serializer_class = PropiedadSerializer
    authentication_classes = [TokenAuthentication]  # Autenticación por token
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados