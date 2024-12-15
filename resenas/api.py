from .models import Resena
from rest_framework import viewsets, permissions
from .serializer import ResenaSerializer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from datetime import datetime

from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
@extend_schema_view(
    retrieve=extend_schema(
        summary="Detalles de una Resena",
        description="Detalles de una reseña en especifico.",
        tags=["Reseñas"]),
    create=extend_schema(
        summary="Crear una Resena",
        description="Crear una nueva reseña.",
        tags=["Reseñas"]),
    update=extend_schema(
        summary="Actualizar una Resena",
        description="Actualizar la información de una reseña existente.",
        tags=["Reseñas"]),
    destroy=extend_schema(
        summary="Eliminar una Resena",
        description="Eliminar una reseña existente.",
        tags=["Reseñas"]),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una Resena",
        description="Actualizar parcialmente la información de una reseña existente.",
        tags=["Reseñas"]),
)


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
    
    # modifico el esquema para el metodo GET indicando que existe el parametro opcional para filtrar por id de propiedad
    @extend_schema(
    summary="Lista de reseñas",
    description="Obtiene una lista de reseñas. Se puede filtrar por ID de propiedad usando el parámetro de consulta `propiedad`.",
    tags=["Reseñas"],
    parameters=[
        OpenApiParameter(
            name="propiedad",
            description="ID de la propiedad para filtrar las reseñas asociadas.",
            required=False,
            type=int, 
        )
    ]
)
    def list(self, request, *args, **kwargs):
        """
        Sobrescribimos este método solo para documentarlo.
        """
        return super().list(request, *args, **kwargs)