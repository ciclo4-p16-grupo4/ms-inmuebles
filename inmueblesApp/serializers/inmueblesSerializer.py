from rest_framework import serializers
from inmueblesApp.models import Inmuebles, ImagenInmuebles
from .imagenesInmuebleSerializer import ImagenInmuebleSerializer

class InmueblesSerializer(serializers.ModelSerializer):
	imagenes = ImagenInmuebleSerializer(many=True, required=False)
	class Meta():
		model = Inmuebles
		fields = ['id','titulo', 'direccion','ciudad', 'poblacion','tipo','precio','area','habitaciones','banos','estrato','contrato','descripcion', 'coordenadas', 'likes', 'imagenes', 'source_mapas']
			
	def create(self, validated_data):
		if 'imagenes' in validated_data.keys():
			imagenesArray = validated_data.pop('imagenes')
		else:
			imagenesArray = []
		inmuebleCreatedInstance = Inmuebles.objects.create(**validated_data)
		for dic in imagenesArray:
			ImagenInmuebles.objects.create(inmueble=inmuebleCreatedInstance,**dict(dic))
		return inmuebleCreatedInstance
	def deleteImagenes(self, validated_data, instance, *args):
		ImagenInmuebles.objects.filter(inmueble_id=instance.id).delete()
	
	def addImages(self, validated_data, instance, imagesArray, *args):
		print(instance)
		for img in imagesArray:
			ImagenInmuebles.objects.create(inmueble=instance, **img)
	
	def update(self, instance, validated_data):
		print(instance.titulo)
		if 'imagenes' in validated_data['newData'].keys():
			imagenes = validated_data['newData'].pop('imagenes')
			imagesArray = [dict(img) for img in imagenes]
			self.deleteImagenes(self, instance)
			self.addImages(self, instance, imagesArray)

		instance.titulo = validated_data['newData'].get('titulo', instance.titulo)
		instance.direccion = validated_data['newData'].get('direccion', instance.direccion)
		instance.ciudad = validated_data['newData'].get('ciudad', instance.ciudad)
		instance.poblacion = validated_data['newData'].get('poblacion', instance.poblacion)
		instance.tipo = validated_data['newData'].get('tipo', instance.tipo)
		instance.precio = validated_data['newData'].get('precio', instance.precio)
		instance.area = validated_data['newData'].get('area', instance.area)
		instance.habitaciones = validated_data['newData'].get('habitaciones', instance.habitaciones)
		instance.banos = validated_data['newData'].get('banos', instance.banos)
		instance.estrato = validated_data['newData'].get('estrato', instance.estrato)
		instance.contrato = validated_data['newData'].get('contrato', instance.contrato)
		instance.descripcion = validated_data['newData'].get('descripcion', instance.descripcion)
		instance.coordenadas = validated_data['newData'].get('coordenadas', instance.coordenadas)
		instance.source_mapas = validated_data['newData'].get('source_mapas', instance.source_mapas)
		instance.likes = validated_data['newData'].get('likes', instance.likes)
		instance.save()

		return instance
	