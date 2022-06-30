from django import forms
from .models import Perro, Dueño

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ['nombre', 'edad', 'raza']

        labels = {
            'nombre': 'Nombre',
            'edad': 'Edad',
            'raza': 'Raza',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
