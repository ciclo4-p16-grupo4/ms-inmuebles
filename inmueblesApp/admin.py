from django.contrib import admin
from .models import Inmuebles
from .models import ImagenInmuebles

# Register your models here.
admin.site.register(Inmuebles)
admin.site.register(ImagenInmuebles)
