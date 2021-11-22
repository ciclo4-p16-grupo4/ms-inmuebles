from rest_framework import serializers
from inmueblesApp.models import Inmuebles, ImagenInmuebles
from .imagenesInmuebleSerializer import ImagenInmuebleSerializer

class InmueblesSerializer(serializers.ModelSerializer):
	imagenes = ImagenInmuebleSerializer(many=True, required=False)
	class Meta():
		model = Inmuebles
		fields = ['id','titulo', 'direccion','ciudad', 'poblacion','tipo','precio','area','habitaciones','banos','estrato','contrato','descripcion', 'coordenadas', 'imagenes']
			
	def create(self, validated_data):
		if 'imagenes' in validated_data.keys():
			imagenesArray = validated_data.pop('imagenes')
		else:
			imagenesArray = []
		inmuebleCreatedInstance = Inmuebles.objects.create(**validated_data)
		for dic in imagenesArray:
			ImagenInmuebles.objects.create(inmueble=inmuebleCreatedInstance,**dict(dic))
		print(inmuebleCreatedInstance.imagenes)
		return inmuebleCreatedInstance
	def deleteImagenes(self, validated_data, instance, *args):
		ImagenInmuebles.objects.filter(inmueble_id=instance.id).delete()
	
	def addImages(self, validated_data, instance, imagesArray, *args):
		print(instance)
		for img in imagesArray:
			ImagenInmuebles.objects.create(inmueble=instance, **img)
	
	def update(self, instance, validated_data):
		print('update.............')
		if 'imagenes' in validated_data.keys():
			imagenes = validated_data.pop('imagenes')
			imagesArray = [dict(img) for img in imagenes]
			self.deleteImagenes(self, instance)
			self.addImages(self, instance, imagesArray)

		instance.titulo = validated_data.get('titulo', instance.titulo)
		instance.direccion = validated_data.get('direccion', instance.direccion)
		instance.ciudad = validated_data.get('ciudad', instance.ciudad)
		instance.poblacion = validated_data.get('poblacion', instance.poblacion)
		instance.tipo = validated_data.get('tipo', instance.tipo)
		instance.precio = validated_data.get('precio', instance.precio)
		instance.area = validated_data.get('area', instance.area)
		instance.habitaciones = validated_data.get('habitaciones', instance.habitaciones)
		instance.banos = validated_data.get('banos', instance.banos)
		instance.estrato = validated_data.get('estrato', instance.estrato)
		instance.contrato = validated_data.get('contrato', instance.contrato)
		instance.descripcion = validated_data.get('descripcion', instance.descripcion)
		instance.save()

		return instance
	