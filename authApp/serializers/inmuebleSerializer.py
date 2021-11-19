from rest_framework import serializers
from authApp.models.inmueble import Inmueble

class InmueblesSerializer(serializers.ModelSerializer):
	class Meta():
		model = Inmueble
		fields = ['nombre', 'direccion','ciudad', 'poblacion','tipo','precio','area','habitaciones','banos','estrato','contrato','descripcion']
			
	def to_representation(self, obj):
		inmuebles = Inmueble.objects.get(id= obj.id)
		return {
            'id': inmuebles.id,
            'nombre': inmuebles.nombre, 
            'direccion': inmuebles.direccion,
            'ciudad': inmuebles.ciudad, 
            'poblacion': inmuebles.poblacion,
            'tipo': inmuebles.tipo,
			'precio': inmuebles.precio,
			'area': inmuebles.area,
			'habitaciones': inmuebles.habitaciones,
			'banos': inmuebles.banos,
			'estrato': inmuebles.estrato,
			'contrato': inmuebles.contrato,
			'descripcion': inmuebles.descripcion,
			'creado': inmuebles.creado,
			'actualizado': inmuebles.actualizado,
        }