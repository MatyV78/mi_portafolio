from django.urls import path
from Proyecto_Vehiculos import views
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("home/", views.home, name="home"),
    path("contacto/", views.contacto, name="contacto"),
    
    #Login, Signup, Logout
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 
    
    
    #Autos Nuevos
    path("add_vehiculo", views.add_vehiculo, name="add_vehiculo"),
    path("Agregar/add_nuevos", views.add_nuevos, name="add_nuevos"),
    path("lista_vNuevos", views.lista_vNuevos, name="lista_vNuevos"),
    path("editar_nuevos/<int:id>", views.editar_nuevos, name="editar_nuevos"),
    path("eliminar_nuevos/<int:id>", views.eliminar_nuevos, name="eliminar_nuevos"),
    path('vehiculo/<int:vehiculo_id>/comentarios/', views.ver_comentarios, name='ver_comentarios'),
    path('vehiculo/<int:vehiculo_id>/comentarios/agregar/', views.agregar_comentario, name='agregar_comentario'),
    path('comentario/<int:comentario_id>/editar/', views.editar_comentario, name='editar_comentario'),
    path('comentario/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    
    #Autos Electricos
    path("Agregar/add_elec", views.add_elec, name="add_elec"),
    path("lista_vElec", views.lista_vElec, name="lista_vElec"),
    path("eliminar_elec/<int:id>", views.eliminar_elec, name="eliminar_elec"),
    path("editar_elec/<int:id>", views.editar_elec, name="editar_elec"),
    path('vehiculo_elec/<int:vehiculo_id>/comentarios/', views.ver_comentarios_elec, name='ver_comentarios_elec'),
    path('vehiculo_elec/<int:vehiculo_id>/comentarios/agregar/', views.agregar_comentario_elec, name='agregar_comentario_elec'),
    path('comentario_elec/<int:comentario_id>/editar/', views.editar_comentario_elec, name='editar_comentario_elec'),
    path('comentario_elec/<int:comentario_id>/eliminar/', views.eliminar_comentario_elec, name='eliminar_comentario_elec'),
    
    #Autos Usados
    path("Agregar/add_usado", views.add_usado, name="add_usado"),
    path("lista_vUsados", views.lista_vUsados, name="lista_vUsados"),
    path("eliminar_usado/<int:id>", views.eliminar_usado, name="eliminar_usado"),
    path("editar_usado/<int:id>", views.editar_usado, name="editar_usado"),
    path('vehiculo_usado/<int:vehiculo_id>/comentarios/', views.ver_comentarios_usados, name='ver_comentarios_usados'),
    path('vehiculo_usado/<int:vehiculo_id>/comentarios/agregar/', views.agregar_comentario_usados, name='agregar_comentario_usados'),
    path('comentario_usado/<int:comentario_id>/eliminar/', views.eliminar_comentario_usados, name='eliminar_comentario_usados'),
    path('comentario_usado/<int:comentario_id>/editar/', views.editar_comentario_usados, name='editar_comentario_usados'),
    
    
    #Marcas y Modelos
    path("marcas_modelos", views.marcas_modelos, name="marcas_modelos"),
    path("agregar_marca", views.agregar_marca, name="agregar_marca"),
    path("eliminar_marca/<int:id>", views.eliminar_marca, name="eliminar_marca"),
    path("editar_marca/<int:id>", views.editar_marca, name="editar_marca"),
    
    path("lista_modelos/<marca_id>/modelos", views.lista_modelos, name="lista_modelos"),
    path("agregar_modelo", views.agregar_modelo, name="agregar_modelo"),
    path("eliminar_modelo/<int:id>", views.eliminar_modelo, name="eliminar_modelo"),
    path("editar_modelo/<int:id>", views.editar_modelo, name="editar_modelo"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
