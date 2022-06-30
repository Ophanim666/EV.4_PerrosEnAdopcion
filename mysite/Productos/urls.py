from django.urls import path
# from django.conf.urls import url
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductoList, ProductoCreate, ProductoUpdate , ProductoDelete
from rest_framework.urlpatterns import format_suffix_patterns
from Productos import views
from .views import API_objects, API_objects_details

urlpatterns = [
    path('listar/', ProductoList.as_view(), name="productos_list"),

    path('crear/', ProductoCreate.as_view(), name="producto_form"),
    path('editar/<int:pk>', ProductoUpdate.as_view(), name="producto_update"),
    path('borrar/<int:pk>', ProductoDelete.as_view(), name="producto_borrar"),
]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = [
    path('api/', API_objects.as_view()),
    path('api/<int:pk>/', API_objects_details.as_view()),
]