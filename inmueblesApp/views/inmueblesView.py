from django.conf                                  import settings
from django.db.models.query import QuerySet
from rest_framework                               import generics, status
from rest_framework.response                      import Response
from rest_framework.permissions                   import SAFE_METHODS, IsAdminUser, IsAuthenticated
from rest_framework.serializers                   import Serializer
from rest_framework_simplejwt.backends            import TokenBackend
from inmueblesApp.models.inmuebles                import Inmuebles
from inmueblesApp.serializers.inmueblesSerializer import InmueblesSerializer

class InmueblesDetailView (generics.RetrieveAPIView):
    queryset = Inmuebles.objects.all()
    serializer_class = InmueblesSerializer
    permission_classes = ()
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class InmueblesCreateView(generics.CreateAPIView):
    queryset = Inmuebles.objects.all()
    serializer_class = InmueblesSerializer

    def post(self, request, *args, **kwargs):
        serializer = InmueblesSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Inmueble añadido exitosamente", status= status.HTTP_201_CREATED)

class InmueblesDeleteView(generics.DestroyAPIView):
    queryset = Inmuebles.objects.all()
    serializer_class = InmueblesSerializer
    

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class InmueblesUpdateView(generics.UpdateAPIView):
    queryset = Inmuebles.objects.all()
    serializer_class = InmueblesSerializer

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)