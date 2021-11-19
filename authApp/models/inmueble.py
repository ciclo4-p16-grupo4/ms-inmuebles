from django.db import models
from datetime import datetime

POBLACION_CHOICES = [
    ('R', 'rural'),
    ('U', 'urbano')
]

TIPO_INMUEBLE_CHOICES = [
    ('CAS', 'Casa'),
    ('APT', 'Apartamento'),
    ('LOC', 'Local')
]

CONTRATO_CHOICES = [
    ('ALQ', 'Alquiler'),
    ('VEN', 'Venta')
]


class Inmueble(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField('Nombre', max_length=40)
    direccion = models.TextField('Direccion', max_length=60)
    ciudad = models.TextField('Ciudad', max_length=15)
    poblacion = models.CharField(max_length=3, choices=POBLACION_CHOICES)
    precio = models.IntegerField()
    tipo = models.CharField(max_length=3, choices=TIPO_INMUEBLE_CHOICES)
    area = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    estrato = models.IntegerField()
    contrato = models.CharField(max_length=3, choices=CONTRATO_CHOICES)
    descripcion = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    coordenadas = models.CharField(max_length=100)