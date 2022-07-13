from django import forms
from django.core.exceptions import ValidationError
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeValidator
from django.forms import ValidationError

class ContactoForms(forms.ModelForm):

    class Meta:
        model= Contacto
      #  fields= ['nombre', 'correo', 'tipo_consulta', 'mensaje', 'avisos'] Uno a uno
        fields = '__all__'


class ProductoForms(forms.ModelForm):

    nombre= forms.CharField(min_length=3, max_length=50)
    imagen= forms.ImageField(required=False, validators=[MaxSizeValidator(max_file_size= 2)])
    precio= forms.IntegerField(min_value=1)

    def clean_nombre(self):
      nombre= self.cleaned_data["nombre"]
      existe= Producto.objects.filter(nombre__iexact= nombre).exists

      if existe:
        raise ValidationError("Este nombre ya existe")

      return nombre

    class Meta:
        model= Producto
        fields = '__all__'
        widgets= {
          "fecha_fabricacion": forms.SelectDateWidget()
        }


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
      model = User
      fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
