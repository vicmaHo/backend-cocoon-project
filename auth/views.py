# Rutas de autenticación, login, register y test de autenticación
from rest_framework.decorators import api_view
from rest_framework.response import Response
from usuarios.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.
@api_view(['POST'])
def register(request):
    """
    Registro de un nuevo usuario en la plataforma, generando un token de autenticación
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    """
    Login de un usuario, generando un token de autenticación
    """
    user =get_object_or_404 (User, username=request.data['username']) 
    
    if not user.check_password(request.data['password']): 
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST) 
    
    token, created = Token.objects.get_or_create(user=user) 
    
    serializer = UserSerializer(instance=user) 
    
    return Response({'token': token.key, 'created': created, 'user': serializer.data}, status=status.HTTP_200_OK)