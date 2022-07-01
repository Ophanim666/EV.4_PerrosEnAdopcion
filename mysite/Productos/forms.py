from .models import Productos
from django import forms

class ProductoForm(forms.ModelForm):
    

    class Meta:
        model = Productos
        fields = (
            'fotografia',
            'nombre',
            # 'precio',
            'grado_productos',
        )
        labels = {
            'fotografia':'Fotografia',
            'nombre':'Nombre',
            # 'precio':'Precio',
            'grado_productos':'Grado_productos'
        }
        widgets = {
            # 'fotografia':forms.FileInput(attrs={'class':'form-control','type':'file'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            # 'precio':forms.TextInput(attrs={'class':'form-control'}),
            'grado_productos':forms.Select(choices="GRADOS_PRODUCTOS", attrs={'class':'form-control'}),
        }

    
