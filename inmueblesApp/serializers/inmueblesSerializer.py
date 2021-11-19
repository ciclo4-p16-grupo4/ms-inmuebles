from rest_framework import serializers
from inmueblesApp.models.inmuebles import Inmuebles

class InmueblesSerializer(serializers.ModelSerializer):
	class Meta():
		model = Inmuebles
		fields = ['nombre', 'direccion','ciudad', 'poblacion','tipo','precio','area','habitaciones','banos','estrato','contrato','descripcion']
			
	def to_representation(self, obj):
		inmuebles = Inmuebles.objects.get(id= obj.id)
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