from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from aplicacion.models import *
from aplicacion.forms import *
# Create your views here.


def formulario_cliente(request):

    if request.method == 'POST':

        formulario_cliente = Formulario_cliente(request.POST) 
        if formulario_cliente.is_valid():

                cliente = Formulario_cliente(nombre_cliente=formulario_cliente.cleaned_data['nombre_cliente'], apellido_cliente=formulario_cliente.cleaned_data['apellido_cliente'], telefono_cliente=formulario_cliente.cleaned_data['telefono_cliente'], email_cliente=formulario_cliente.cleaned_data['email_cliente'])

                cliente.save()

                return render(request, "formulario_cliente.html")
    else: 

        formulario_cliente= Formulario_cliente() 

        return render(request, "padre.html", {"formulario_cliente": formulario_cliente})


def formulario_paseador(request):

    if request.method == 'POST':

        formulario_paseador = Formulario_paseador(request.POST) 
        if formulario_paseador.is_valid():

            paseador = Paseador (nombre_cliente=informacion['nombre'], apellido_cliente=informacion['apellido'], telefono_cliente=informacion['telefono'], email_cliente=informacion['email']) 

            paseador.save()

            return render(request, "formulario_paseador.html")
    else: 

        formulario_paseador = Datos_paseador() 

        return render(request, "padre.html", {"formulario_paseador": formulario_paseador})

def padre(request):
    return render(request,'padre.html')

