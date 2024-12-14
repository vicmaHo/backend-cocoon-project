# Rutas de autenticación, login, register y test de autenticación
from rest_framework.decorators import api_view
from rest_framework.response import Response
from auth.serializer import PasswordResetRequestSerializer, PasswordResetSerializer
from usuarios.serializers import UserSerializer, ArrendatarioSerializer, ArrendadorSerializer, EstudianteSerializer
from usuarios.models import Usuario, Arrendatario, Arrendador, Estudiante
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404


# Para recuperacion de contrasena
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from decouple import config



# Create your views here.
@api_view(['POST'])
def register(request):
    
    """
    Registro de un nuevo usuario en la plataforma, generando un token de autenticación
    Primero comprueba que tipo de usuario se va a registrar para despues crear un User de Django
    Luego crea un Usuario perteneciente al modelo propio, en base a esos crea el tipo de usuario
    que se mande en la petición.
    """
    # Compruebo si el tipo de usuario es arrendaddor
    if request.data["is_arrendador"] == True:
       # si es arrendador creo un User luego un Usuario y despues un Arrendador 
        user_data = extraer_datos_usuario(request)
        # Creo el serializer
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            
            user = crear_user(serializer)
            user.save()
            
            # Creo el Usuario del modelo propio
            usuario = crear_usuario_normal(serializer, request, 'arrendador')
            usuario.save()
            
            # Creo el Arrendador
            arrendador = Arrendador.objects.create(
                usuario = usuario,
                ocupacion = request.data['ocupacion']
            )
            arrendador.save()
            
            # Creo el token
            token = Token.objects.create(user=user)
            arrendador_serializer = ArrendadorSerializer(arrendador)
            return Response({'token': token.key, 'tipo': usuario.tipo,'created': True, 'datos': arrendador_serializer.data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    elif request.data["is_estudiante"] == True:
        
        user_data = extraer_datos_usuario(request)
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            user = crear_user(serializer)
            user.save()
            
            # Creo el usuario del modelo propio
            usuario = crear_usuario_normal(serializer, request, 'estudiante')
            usuario.save()
            
            # Creo arrendatario
            arrendatario = Arrendatario.objects.create(
                usuario = usuario,
            )
            arrendatario.save()
            
            # Creo el estudiante
            estudiante = Estudiante.objects.create(
                arrendatario = arrendatario,
                constancia_universidad = request.data['constancia_universidad'],
                universidad = request.data['universidad']
            )
            estudiante.save()
            
            # Creo el token
            token = Token.objects.create(user=user)
            estudiante_serializer = EstudianteSerializer(estudiante)
            
            return Response({'token': token.key,
                             'tipo': usuario.tipo,
                             'created': True,
                            'datos': estudiante_serializer.data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    else: 
        user_data = extraer_datos_usuario(request)
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            user = crear_user(serializer)
            user.save()
            
            # Creo el usuario del modelo propio
            usuario = crear_usuario_normal(serializer, request, 'arrendatario')
            usuario.save()
            
            # Creo arrendatario
            arrendatario = Arrendatario.objects.create(
                usuario = usuario
            )
            
            arrendatario.save()
            
            token = Token.objects.create(user=user)
            
            arrendatario_serializer = ArrendatarioSerializer(arrendatario)
            return Response({'token': token.key,
                             'tipo': usuario.tipo,
                             'created': True,
                             'datos': arrendatario_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    """
    Login de un usuario, generando un token de autenticación y mandando el tipo de usuario junto
    con sus respectivos datos principales.
    """
    user =get_object_or_404 (User, username=request.data['username'])
    
    if not user.check_password(request.data['password']):
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    
    tipo_usuario = Usuario.objects.get(user_id=user.id).tipo
    
    serializer = UserSerializer(instance=user)
    
    return Response({'token': token.key, 'tipo': tipo_usuario,'created': created, 'datos': serializer.data}, status=status.HTTP_200_OK)


#### Funciones Auxiliares ####
def extraer_datos_usuario(request):
    user_data = {'username': request.data['username'], 
                'email': request.data['email'], 
                'password': request.data['password'],
                'last_name': request.data['last_name'],
                'first_name': request.data['first_name']
                }
    return user_data

def crear_user(serializer):
    serializer.save()
    user = User.objects.get(username=serializer.data['username'])
    user.set_password(serializer.data['password'])
    user.email = serializer.data['email']
    user.first_name = serializer.data['first_name']
    user.last_name = serializer.data['last_name']
    # Debo retornar el objeto y guardarlo en donde lo vaya a usar
    return user

def crear_usuario_normal(serializer, request, tipo):
    usuario = Usuario.objects.create(
        user=User.objects.get(username=serializer.data['username']),
        telefono = request.data['telefono'],
        tipo = tipo,
        profile_picture = request.data['profile_picture']
    )
    return usuario      


#### recuperacion de contrasena ####
class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = get_object_or_404(User, email=email)
            
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            
            #f"http://frontend/reset-password/{uid}/{token}/
            reset_url = f"{config('FRONTEND_URL', default='http://frontend/')}reset-password/{uid}/{token}/"
            send_mail(
                "Recuperación de Contraseña",
                f"Usa este enlace para restablecer tu contraseña: {reset_url}",
                "cocoon.homeapp@gmail.com",
                [email]
            )
            return Response({"message": "Email enviado con instrucciones para recuperar contraseña."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# proceso de la nueva contrasena
class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contraseña restablecida exitosamente."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)