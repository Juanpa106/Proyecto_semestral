from rest_framework import serializers
from app.models import *

#CRUD DESDE API
class Producto_TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto_Tienda
        fields = '__all__'