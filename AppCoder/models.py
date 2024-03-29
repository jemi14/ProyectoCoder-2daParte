from unittest.util import _MAX_LENGTH
from django.db import models

#---------------Clase 24-------------------------------
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

# Create your models here.

class Curso(models.Model):
#esto genera la tabla para la base de datos
    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada}"

#-------------------------------------------------------------------
class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

#-------------------------------------------------------------------
class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

#---------------Clase 22-------------------------------
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email} - Profesión: {self.profesion}"

#-------------------------------------------------------------------
class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega= models.DateField()
    entregado= models.BooleanField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de entrega: {self.fechaDeEntrega} - Entregado: {self.entregado}"

#---------------Clase 24-------------------------------
class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcarpeta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True) 