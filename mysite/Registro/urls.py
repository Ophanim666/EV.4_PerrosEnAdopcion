from django.urls import path, include
from . import views

urlpatterns = [
    # listar perros
    path('listarPerros', views.listar_perros, name="listar_perros"),
    # agregar perro
        # agregar una carrera    
    path('agregarPerro', views.agregar_perro, name="agregar_perro"),
    
    # OTROS LLAMADOS CON GENERICS
    # llamando a la clases 
    path('add_perro', views.PerroCreate.as_view(), name="add_perro"),

    path('list_perros/', views.PerroList.as_view(), name='list_perros'),

    path('edit_perro/<int:pk>', views.PerroUpdate.as_view(), name='edit_perro'),

    path('del_perro/<int:pk>', views.PerroDelete.as_view(), name='del_perro'),

    # API
    path('perros/',  views.perro_collection , name='perro_collection'),
    path('perros/<int:pk>/', views.perro_element ,name='perro_element'),
    
    # con log in y log out
    # editar una carrera
    # path('editar_carrera/<int:carrera_id>', login_required(views.editar_carrera), name="editar_carrera"),

    # borrar una carrera
    # path('borrar_carrera/<int:carrera_id>', login_required(views.borrar_carrera), name="borrar_carrera"),
    
    
    # borrar
    path('home',views.home, name='home'), 
    path('identificador_de_razas.html', views.iden_razas, name='iden_razas'),
    
    # ------------------------------------------------------------------------------------------------------------------------------

]
