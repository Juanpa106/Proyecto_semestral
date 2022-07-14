from django.contrib import admin
from .models import Tipo_Producto, Producto_Tienda
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio", "marca", "stock"]
    search_fields =["nombre"]
    list_per_page = 5


admin.site.register(Tipo_Producto)
admin.site.register(Producto_Tienda, ProductoAdmin)