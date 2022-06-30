from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Productos
from .forms import ProductoForm

#---------------- las importaciones para la API ------------
from rest_framework import generics
from .serializer import ProductosSerializer
# token
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class ProductoList (ListView):                    
    model = Productos
    template_name = 'Productos/producto_list.html'

class  ProductoCreate (CreateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'Productos/producto_form.html'
    success_url = reverse_lazy('productos_list')

class  ProductoUpdate(UpdateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'Productos/producto_form.html'
    success_url = reverse_lazy('productos_list')

class  ProductoDelete(DeleteView):
    model = Productos
    template_name = 'Productos/producto_borrar.html'
    success_url = reverse_lazy('productos_list')



# api

class API_objects(generics.ListCreateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
