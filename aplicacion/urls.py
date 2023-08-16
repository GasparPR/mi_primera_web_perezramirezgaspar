from django.urls import path
from . import views

urlpatterns = [
    #path('datos_cliente/' , views.Datos_cliente , name='datos_cliente'),
    #path('datos_paseador/' , views.Datos_paseador , name='datos_paseador'),
    #path('mascota/' , views.mascota , name='mascota'),
    #path('crear_cliente/', views.formulario_cliente , name='crear_cliente'),
    path('crear_paseador/', views.formulario_paseador , name='crear_paseador'),
    path('padre/', views.padre, name='padre'),
    path('Mascota/', views.Mascota, name='Mascota'),
    path('formulario_cliente/', views.formulario_cliente , name='formulario_cliente'),
]