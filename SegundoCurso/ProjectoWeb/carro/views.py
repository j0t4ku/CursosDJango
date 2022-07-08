from django.shortcuts import render
from .carro import Carro
from Tienda.models import Producto
from django.shortcuts import redirect

# Create your views here.

def AgregarProducto(request, producto_id):
    carro= Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.Agregar(producto=producto)
    return redirect("tienda")

def EliminarProducto(request, producto_id):
    carro= Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.Eliminar(producto=producto)
    return redirect("tienda")

def RestarProducto(request, producto_id):
    carro= Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.Restar(producto=producto)
    return redirect("tienda")

def LimpiarCarro(request):
    carro= Carro(request)
    carro.Limpiar()
    return redirect("tienda")