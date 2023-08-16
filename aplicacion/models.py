from django.db import models

# Create your models here.

class Datos_cliente(models.Model):
    nombre_cliente = models.CharField(max_length=40)
    apellido_cliente = models.CharField(max_length=40)
    email_cliente = models.EmailField()
    telefono_cliente = models.IntegerField()

class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=40)
    tamanio_mascota = models.CharField(max_length=40)
    peso_mascota = models.IntegerField()

class Datos_paseador(models.Model):
    nombre_paseador = models.CharField(max_length=40)
    apellido_paseador = models.CharField(max_length=40)
    email_paseador = models.EmailField()
    telefono_paseador = models.IntegerField()