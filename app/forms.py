from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto_Tienda
        fields = '__all__'

class CustomCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]


class subscripcionForm(forms.ModelForm):
    class Meta:
        model = Subscripcion
        fields = ['username', 'suscrito']