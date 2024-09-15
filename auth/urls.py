from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    
    ## Agrego rutas
    path('register', views.register),
    path('login', views.login),
    

    
    # path('profile', views.profile),
    
]
