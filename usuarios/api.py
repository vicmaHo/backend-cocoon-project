from .models import Arrendador, Arrendatario, Estudiante
from rest_framework import viewsets, permissions
from .serializers import ArrendadorSerializer, ArrendatarioSerializer, EstudianteSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from drf_spectacular.utils import extend_schema_view, extend_schema
@extend_schema_view(
    list=extend_schema(
        summary="Listado de Arrendadores",
        description="Listado todos los Arrendadores existentes en la base de datos de Coccon-Home",
        tags=["Usuarios-Arrendador"]),
    retrieve=extend_schema(
        summary="Detalles de un Arrendador",
        description="Detalles de un Arrendador en específico",
        tags=["Usuarios-Arrendador"]),
    create=extend_schema(
        summary="Crear un Arrendador",
        description="Crear un Arrendador",
        tags=["Usuarios-Arrendador"], exclude=True),
    update=extend_schema(
        summary="Actualizar un Arrendador",
        description="Actualizar la información de un Arrendador",
        tags=["Usuarios-Arrendador"]),
    destroy=extend_schema(
        summary="Eliminar un Arrendador",
        description="Eliminar un Arrendador",
        tags=["Usuarios-Arrendador"]),
    partial_update=extend_schema(tags=["Usuarios-Arrendador"], exclude=True),
)
# ViewSet-> Quien puede consultar mi modelo, Realización de operaciones basicas crud par ael modelo Project
class ArrendadorViewSet(viewsets.ModelViewSet):
    #indico la consulta
    queryset= Arrendador.objects.all()
    # permission_classes = [permissions.AllowAny] 
    serializer_class = ArrendadorSerializer
    authentication_classes = [TokenAuthentication]  # Autenticación por token
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados

@extend_schema_view(
    list=extend_schema(
        summary="Listado de Arrendatarios",
        description="Listado todos los Arrendatarios existentes en la base de datos de Coccon-Home",
        tags=["Usuarios-Arrendatario"]),
    retrieve=extend_schema(
        summary="Detalles de un Arrendatario",
        description="Detalles de un Arrendatario en específico",
        tags=["Usuarios-Arrendatario"]),
    create=extend_schema(tags=["Usuarios-Arrendatario"],exclude=True),
    update=extend_schema(
        summary="Actualizar un Arrendatario",
        description="Actualizar la información de un Arrendatario",
        tags=["Usuarios-Arrendatario"]),
    destroy=extend_schema(
        summary="Eliminar un Arrendatario",
        description="Eliminar un Arrendatario",
        tags=["Usuarios-Arrendatario"]),
    partial_update=extend_schema(tags=["Usuarios-Arrendatario"],exclude=True),
)

class ArrendatarioViewSet(viewsets.ModelViewSet):
    queryset= Arrendatario.objects.all()
    serializer_class = ArrendatarioSerializer
    authentication_classes = [TokenAuthentication]  # Autenticación por token
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados

# @extend_schema(exclude=True)  # Este endpoint no aparecerá en Swagger
@extend_schema_view(
    list=extend_schema(
        summary="Listado de Estudiantes",
        description="Listado todos los Estudiantes existentes en la base de datos de Coccon-Home",
        tags=["Usuarios-Estudiante"]),
    retrieve=extend_schema(
        summary="Detalles de un Estudiante",
        description="Detalles de un Estudiante en específico",
        tags=["Usuarios-Estudiante"]),
    create=extend_schema(tags=["Usuarios-Estudiante"],exclude=True),
    update=extend_schema(
        summary="Actualizar un Estudiante",
        description="Actualizar la información de un Estudiante",
        tags=["Usuarios-Estudiante"]),
    destroy=extend_schema(
        summary="Eliminar un Estudiante",
        description="Eliminar un Estudiante",
        tags=["Usuarios-Estudiante"]),
    partial_update=extend_schema(tags=["Usuarios-Estudiante"],exclude=True),
)
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset= Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    authentication_classes = [TokenAuthentication]  # Autenticación por token
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados