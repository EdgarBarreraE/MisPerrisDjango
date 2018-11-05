from django.db import models

from PIL import Image

# Create your models here.

class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    fechaNacimiento = models.DateField()
    telefono = models.IntegerField()
    tipoCasa = models.CharField(max_length=30)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)


class Rescatado(models.Model):
    foto = models.ImageField(upload_to='fotos/')
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    descripcion = models.TextField()
    estado = models.IntegerField(default=1)