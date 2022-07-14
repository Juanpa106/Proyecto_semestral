from django.db import models

# Create your models here.

class Tipo_Producto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre




class Producto_Tienda(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.CharField(max_length=50)
    stock = models.IntegerField()
    tipo = models.ForeignKey(Tipo_Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)


    def __str__(self):
        return self.nombre



class Carrito_Compras(models.Model):
    nombre_producto = models.CharField(max_length=50)
    precio_producto = models.IntegerField()
    marca_producto = models.CharField(max_length=50)
    imagen_producto = models.ImageField(upload_to = "carrito_compras",null= True)
    cantidad = models.IntegerField()



    class Meta:
        db_table = 'db_Carrito'




class Historial(models.Model):
    codigo = models.ForeignKey(Carrito_Compras, on_delete= models.CASCADE)

    class Meta:
        db_table = 'Historial'


###########################
class TipoUsuario(models.Model):
    tipo= models.CharField(max_length=25)

    def __str__(self):
        return self.tipo
    
    class Meta:
        db_table ='db_Tipo_usuario'

class usuario(models.Model):
    run=models.IntegerField(null=False,primary_key=True)
    nombre=models.CharField(max_length=30)
    correo=models.CharField(max_length=30)
    numero=models.CharField(max_length=12)
    tipo=models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.run

    class Meta:
        db_table ='db_Usuario'


#######################################
class Subscripcion(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    suscrito =  models.BooleanField(default=False)

    def __str__(self):
        return self.suscrito

    class Meta:
        db_table = 'db_Subscripcion'



    



        
