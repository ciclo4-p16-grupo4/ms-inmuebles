from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, IsAuthenticated
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.backends import TokenBackend
from inmueblesApp.models.inmuebles import Inmuebles
from inmueblesApp.serializers.inmueblesSerializer import InmueblesSerializer

class InmueblesDetailView (generics.RetrieveAPIView):
    queryset = Inmuebles.objects.all()
    serializer_class = InmueblesSerializer
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class InmueblesCreateView(generics.CreateAPIView):
    queryset = Inmuebles.objects.all()
    serializer_class = InmueblesSerializer

    def post(self, request, *args, **kwargs):
        serializer = InmueblesSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Inmueble añadido exitosamente","data": serializer.data}, status= status.HTTP_201_CREATED)

class InmueblesDeleteView(generics.DestroyAPIView):
    def delete(self, request, id):
        deleted = Inmuebles.objects.filter(id=id).delete()
        if(not deleted[1]):
            return Response({"detail": "inmueble with id "+str(id)+" Not Found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "deleted", "data": deleted[1]}, status=status.HTTP_200_OK)

class InmueblesUpdateView(views.APIView):
    def put(self, request, id):
        updateInmuebleInstance = Inmuebles.objects.get(id=id)
        updateInmuebleSerializer = InmueblesSerializer(updateInmuebleInstance, data=request.data)
        updateInmuebleSerializer.is_valid(raise_exception=True)
        updateInmuebleSerializer.save()
        return Response({"detail": "succes", "data": updateInmuebleSerializer.data}, status=status.HTTP_200_OK)