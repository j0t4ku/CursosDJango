from django.shortcuts import render, redirect

from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib import messages
# Create your views here.


class VRegistro(View):
    
    def get(self, request):
        form= UserCreationForm()
        return render(request, "authenticacion/registro.html", {"form":form})


    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
        
            return render(request, "authenticacion/registro.html", {"form":form})


def Logout(request):
    logout(request)
    return redirect('home')


def Login(request):

    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usuario= authenticate(username=nombre_username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "Usuario o contraseña no es valida")
            
        else:
            messages.error(request, "Usuario o contraseña no es valida")
    form= AuthenticationForm()
    return render(request, "authenticacion/login.html", {"form":form})

