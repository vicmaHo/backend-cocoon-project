from rest_framework import routers
from .api import ArrendadorViewSet, ArrendatarioViewSet, EstudianteViewSet



# Creación automatica de las rutas
router = routers.DefaultRouter() # instancia que me permite la creación automatica de rutas para todas las operaciones crud


router.register('api/arrendadores', ArrendadorViewSet, 'arrendadores') # ruta, viewset, nombre
router.register('api/arrendatarios', ArrendatarioViewSet, 'arrendatarios')
router.register('api/estudiantes', EstudianteViewSet, 'estudiantes')


urlpatterns = router.urls # agrego a url patters que posteriormente incluyo en el url main del proyecto