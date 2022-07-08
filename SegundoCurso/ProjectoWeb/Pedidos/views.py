
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Pedidos.models import LineaPedido, Pedido
from carro.carro import Carro
from django.contrib import messages

# Create your views here.


@login_required(login_url="/auth/login")
def ProcesarPedido(request):
    pedido= Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedidos=list()
    for key,value in carro.carro.items():
        lineas_pedidos.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedidos)
    enviar_mail(pedido=pedido, lineas= lineas_pedidos, ususario=request.username, email= request.usermail)
    messages.success(request,"Se ha realizado El pedido correctamente")
    return redirect("../tienda")


def enviar_mail(producto_id,cantidad,user,pedido):
    pass

