from django.shortcuts import render
from .models import CategoriaProd, Producto
# Create your views here.



def categoriaProd(request, categoria_id):
    cat= CategoriaProd.objects.get(id= categoria_id)
    prod=Producto.objects.filter(categorias=cat)
    return render(request, "tienda/categorias.html", {"categorias":cat, "prod":prod})

def tienda(request):
    producto= Producto.objects.all()
    return render(request, "tienda/tienda.html", {"prod": producto})