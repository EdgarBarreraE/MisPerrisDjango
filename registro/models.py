from django.db import models


# Create your models here.

class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    fechaNacimiento = models.DateField('%m/%d/%Y')
    telefono = models.IntegerField()
    tipoCasa = models.CharField(max_length=100)
    region = models.CharField(max_length=80)
    comuna = models.CharField(max_length=80)
