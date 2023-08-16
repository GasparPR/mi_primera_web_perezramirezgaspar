from django import forms

class Formulario_cliente(forms.Form):
    nombre_cliente = forms.CharField(max_length=40, label ='Nombre cliente')
    apellido_cliente = forms.CharField(max_length=40, label = 'Apellido cliente')
    email_cliente = forms.EmailField()
    telefono_cliente = forms.IntegerField()

class Formulario_paseador(forms.Form):
    nombre_paseador = forms.CharField(max_length=40, label ='Nombre paseador')
    apellido_paseador = forms.CharField(max_length=40, label = 'apellido paseador')
    email_paseador = forms.EmailField()
    telefono_paseador = forms.IntegerField()

class Mascota(forms.Form):
    nombre_mascota = forms.CharField(max_length=40,label = 'nombre mascota' )
    tamanio_mascota = forms.CharField(max_length=40,label = 'Tamanio de la mascota')
    peso_mascota = forms.IntegerField()