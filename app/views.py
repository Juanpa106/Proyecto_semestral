from itertools import count
import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group


# Create your views here.

def home(request):
    response = requests.get('http://127.0.0.1:8000/api/Producto_Tienda/').json()
    productos = Producto_Tienda.objects.all()
    data={
        'ProductosTienda': productos,
        'ListaJson' : response
    }
    if request.method == 'POST':
        carrito = Carrito_Compras()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.marca_producto = request.POST.get('marca_producto')
        carrito.imagen_producto = request.POST.get('imagen_producto')
        carrito.cantidad = request.POST.get('stock')
        carrito.precio_producto = int(carrito.cantidad) * int(carrito.precio_producto)
        carrito.save()




    return render(request, 'app/home.html',data)

@login_required
def carrito(request):
    carrito = Carrito_Compras.objects.all()
    data = {
        'ListaCarrito' : carrito
    }
    return render(request, 'app/carrito.html', data)


def eliminar_productcart(request, id):
    productocarrito = get_object_or_404(Carrito_Compras, id=id)
    productocarrito.delete()
    return redirect(to="carrito")

def registro(request):
    data = {
         'form': CustomCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)



@permission_required('app.add_producto')
def agregar_producto(request):
    data = {

        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Agregado Correctamente"
        else:
            data["form"] = formulario
                
    return render(request,'app/producto/agregar.html', data)


@permission_required('app_view_producto')
def listar_producto(request):
    productos = Producto_Tienda.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'app/producto/listar.html', data)


@permission_required('app.change_producto')
def modificar_producto(request, id):
    producto = get_object_or_404(Producto_Tienda, id=id)

    data ={
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
            data["form"] = formulario
    return render(request, 'app/producto/modificar.html', data)


@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto_Tienda, id=id)
    producto.delete()
    return redirect(to="listar_producto")



def pago(request):
    carrito = Carrito_Compras.objects.all()
    carrito.delete()

    return render(request, 'app/pago.html')


def pag_api(request):
    response1 = requests.get('https://api.waifu.im/random/?selected_tags=selfies').json()
    data={
        'Listapi' : response1['images']
    }
    return render(request,'app/api.html',data)



#########################
def subscripcion(request):
    subscripcionAll = Subscripcion.objects.all()
    datos = {
        'listaSuscripcion' : subscripcionAll,
        'form': subscripcionForm(),
        'usuario' : 0
    }

    usuario= request.user.username

    if Subscripcion.objects.filter(username=usuario).exists():
        datos['usuario'] = 1

    if request.method == 'POST':
        subscripcion=Subscripcion()
        subscripcion.username = request.POST.get('username')
        subscripcion.suscrito = True
        subscripcion.save()
        return redirect(to="subscripcion")
    return render(request, 'app/subscripcion.html', datos)



