from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import productos_a 
from .forms import ProductosForm

#---------------- las importaciones para la API ------------
from rest_framework import generics
from .serializers import ProductosSerializer
# ---------------------------------------------------------
# 23/06/2022
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# from django.contrib.auth.models import User

# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
        
# Este código se activa cada vez que se 
# crea un nuevo usuario y se guarda en la base de datos.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
# ---------------------------------------------------------------------


class ProductosList (ListView):                    
    model = productos_a 
    template_name = 'Productos_a/producto_list.html'

class ProductosCreate (CreateView):
    model = productos_a 
    form_class = ProductosForm
    template_name = 'Productos_a/producto_form.html'
    success_url = reverse_lazy('productos_list')

class ProductosUpdate(UpdateView):
    model = productos_a 
    form_class = ProductosForm
    template_name = 'Productos_a/producto_form.html'
    success_url = reverse_lazy('productos_list')

class ProductosDelete(DeleteView):
    model = productos_a 
    template_name = 'Productos_a/producto_borrar.html'
    success_url = reverse_lazy('productos_list')


# ------------------ API REST --------
class API_objects(generics.ListCreateAPIView):
    queryset = productos_a .objects.all()
    serializer_class = ProductosSerializer
    
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = productos_a .objects.all()
    serializer_class = ProductosSerializer



