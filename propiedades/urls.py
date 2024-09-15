from rest_framework import routers
from .api import PropiedadViewSet


# Creación automatica de las rutas
router = routers.DefaultRouter() # instancia que me permite la creación automatica de rutas para todas las operaciones crud


router.register('api/propiedades', PropiedadViewSet, 'propiedades') # ruta, viewset, nombre


urlpatterns = router.urls # agrego a url patters que posteriormente incluyo en el url main del proyecto
