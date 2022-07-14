from .models import productos_a 
from django import forms

class ProductosForm(forms.ModelForm):
    

    class Meta:
        model = productos_a 
        fields = (
            'fotografia',
            'codigo',
            'nombre',
            'categoria'
        )
        labels = {
            'fotografia':'Fotografia',
            'codigo':'Codigo',
            'nombre':'Nombre',
            'categoria':'Categoria',
        }
        widgets = {
            'fotografia':forms.FileInput(attrs={'class':'form-control','type':'file'}),
            'codigo':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(choices="CATEGORIAS", attrs={'class':'form-control'}),
        }



