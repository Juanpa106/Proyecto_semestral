from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('carrito/', carrito, name="carrito"),
    path('registro/', registro, name="registro"),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('listar_producto/', listar_producto, name="listar_producto"),
    path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('eliminar_productcart/<id>/', eliminar_productcart, name="eliminar_productcart"),
    path('pago/', pago, name="pago"),
    path('pag_api', pag_api, name="pag_api"),
    path('subscripcion', subscripcion, name="subscripcion"),

]
