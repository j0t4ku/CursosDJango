from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.


def contacto(request):
    formulario= FormularioContacto()
    if request.method == "POST":
        formulario= FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
         #   email= EmailMessage("Mensaje Desde AppDJANGO",
         #   "El Sr/a {} con email: {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido),"",["El email del settings"], reply_to=[email])
         #   try:
         #       email.send()
         #   
            return redirect("/contacto/?valido")
         #   except:
         #       return redirect("/contacto/?error")

    return render(request, "contacto/contacto.html", {'formulario':formulario})