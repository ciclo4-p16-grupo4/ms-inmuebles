from django.db import models
from datetime import datetime
from django.core import validators
from .inmuebles import Inmuebles

class ImagenInmuebles(models.Model):
	id = models.AutoField(primary_key=True)
	creado = models.DateTimeField(auto_now_add=True)
	actualizado = models.DateTimeField(auto_now=True)
	url = models.TextField(validators=[validators.URLValidator])
	inmueble = models.ForeignKey(Inmuebles, related_name="imagenes", on_delete=models.CASCADE)