from django.shortcuts import render
from rest_framework import viewsets
from app.models import *
from .serializers import *
# Create your views here.

#MUESTRA DATA DE API
class Producto_TiendaViewSet(viewsets.ModelViewSet):
    queryset = Producto_Tienda.objects.all()
    serializer_class = Producto_TiendaSerializer