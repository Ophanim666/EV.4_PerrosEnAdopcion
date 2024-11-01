from enum import auto
from django.shortcuts import render, redirect
from requests import request
from .models import Perro
from .forms import PerroForm

# las clases genericas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# esta libreria nos permitira redireccionamiento
from django.urls import reverse_lazy

#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PerroSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


# listar perros
def listar_perros(request):
    perros = Perro.objects.all()
    return render(request, "Registro/listar_perros.html", {'perros': perros})

# agregar perro
def agregar_perro(request):
    if request.method == "POST":
        form = PerroForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_perro")
    else:
        form = PerroForm()
        return render(request, "Registro/agregar_perro.html", {'form': form})



#------------CLASES GENERICS-----------------------------------------------
class PerroCreate(CreateView):
    model = Perro
    form_class = PerroForm
    template_name = 'Registro/perro_form.html'
    success_url = reverse_lazy("add_perro")
    


class PerroList(ListView):
    model = Perro
    template_name = 'Registro/list_perros.html'
    # paginate_by = 4

class PerroUpdate(UpdateView):
    model = Perro
    form_class = PerroForm
    template_name = 'Registro/perro_form.html'
    success_url = reverse_lazy('list_perros')

        

class PerroDelete(DeleteView):
    model = Perro
    template_name = 'Registro/perro_delete.html'
    success_url = reverse_lazy('list_perros')


#=============== API REST ===========================
# El decorador @api_view verifica que la solicitud HTTP apropiada 
# se pase a la función de vista. En este momento, solo admitimos solicitudes GET
@api_view(['GET', 'POST'])
def perro_collection(request):
    if request.method == 'GET':
        perros = Perro.objects.all()
        serializer = PerroSerializer(perros, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PerroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def perro_element(request, pk):
    perro = get_object_or_404(Perro, id=pk)

    if request.method == 'GET':
        serializer = PerroSerializer(perro)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        perro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        perro_new = JSONParser().parse(request) 
        serializer = PerroSerializer(perro, data=perro_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# borrar
def home(request):
    return render(request, 'home.html')

def iden_razas(request):
    return render(request, 'identificador_de_razas.html')
