from .models import Arrendador, Arrendatario, Estudiante
from rest_framework import viewsets, permissions
from .serializers import ArrendadorSerializer, ArrendatarioSerializer, EstudianteSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# ViewSet-> Quien puede consultar mi modelo, Realización de operaciones basicas crud par ael modelo Project
class ArrendadorViewSet(viewsets.ModelViewSet):
    #indico la consulta
    queryset= Arrendador.objects.all()
    # permission_classes = [permissions.AllowAny] 
    serializer_class = ArrendadorSerializer
    authentication_classes = [TokenAuthentication]  # Autenticación por token
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados

class ArrendatarioViewSet(viewsets.ModelViewSet):
    queryset= Arrendatario.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = ArrendatarioSerializer
    
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset= Estudiante.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EstudianteSerializer