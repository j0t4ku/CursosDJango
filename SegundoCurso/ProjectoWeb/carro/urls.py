from django.urls import path
from . import views

app_name="carro"
urlpatterns = [
    path("agregar/<int:producto_id>/", views.AgregarProducto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.EliminarProducto, name="eliminar"),
    path("restar/<int:producto_id>/", views.RestarProducto, name="restar"),
    path("limpiar/", views.LimpiarCarro, name="limpiar"),
]
