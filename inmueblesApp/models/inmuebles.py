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


class Inmuebles(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField(max_length=200, db_index=True)
    direccion = models.TextField(max_length=100, db_index=True)
    ciudad = models.TextField(max_length=100, db_index=True)
    poblacion = models.CharField(max_length=3, choices=POBLACION_CHOICES)
    precio = models.DecimalField(max_digits=12,decimal_places=0)
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
