from django.contrib import admin
from django.urls import path
from . import views
from .views import PasswordResetRequestView, PasswordResetView

urlpatterns = [

    
    ## Agrego rutas
    path('register', views.register),
    path('login', views.login),
    
    # recuperacion de contrasena
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),

    
    
]
