from rest_framework import serializers
from inmueblesApp.models import ImagenInmuebles
from inmueblesApp.models import Inmuebles
from rest_framework import serializers


class ImagenInmuebleSerializer(serializers.ModelSerializer):
	class Meta():
		model = ImagenInmuebles
		fields = ['id', 'creado', 'actualizado', 'url']