from django.urls import path, include
from rest_framework import routers
from .views import *

#RUTA DEL API
router = routers.DefaultRouter()
router.register('Producto_Tienda', Producto_TiendaViewSet)


urlpatterns = [
  path('api/', include(router.urls)),
]


