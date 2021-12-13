from django.db.models.query import QuerySet
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from inmueblesApp.models.inmuebles import Inmuebles
from inmueblesApp.serializers.inmueblesSerializer import InmueblesSerializer
from django.db.models import Q

class ImnuebleSearch(views.APIView):
    def get(self, request):
        
        queryConfig = {
            "q": "",
            "searchBy": "titulo",
            "orderBy": "id",
            "sort": "",
            "offset": 0,
            "limit": 10
        }

        if "q" in request.GET.keys():
            queryConfig['q'] = str(request.GET['q'])
        if "limit" in request.GET.keys():
            queryConfig['limit'] = int(request.GET['limit'])
        if "offset" in request.GET.keys():
            queryConfig['offset'] = int(request.GET['offset'])
        if "order_by" in request.GET.keys():
            queryConfig['orderBy'] = request.GET['order_by']
        if "sort" in request.GET.keys():
            if request.GET['sort'] == "DESC":
                queryConfig['sort'] = "-"	
        try:
            inmeblesAll = Inmuebles.objects.filter(Q(titulo__icontains=queryConfig['q']) | Q(direccion__icontains=queryConfig['q']))
            inmueblesQuery = inmeblesAll.order_by(queryConfig['sort']+queryConfig['orderBy'])[queryConfig['offset']:queryConfig['limit']]
            InmuebleSerilizer = InmueblesSerializer(inmueblesQuery, many=True)
            return Response({"count": inmeblesAll.count(), "results": InmuebleSerilizer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Error", "data": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ImnueblesAllView(views.APIView):
    def get(self, request):

        queryConfig = {
            "orderBy": "id",
            "sort": "",
            "offset": 0,
            "limit": 10
        }
        if "limit" in request.GET.keys():
            queryConfig['limit'] = int(request.GET['limit'])
        if "offset" in request.GET.keys():
            queryConfig['offset'] = int(request.GET['offset'])
        if "order_by" in request.GET.keys():
            queryConfig['orderBy'] = request.GET['order_by']
        if "sort" in request.GET.keys():
            if request.GET['sort'] == "DESC":
                queryConfig['sort'] = "-"	        
        try:
            inmeblesAll = Inmuebles.objects.all()
            inmueblesQuery = inmeblesAll.order_by(queryConfig['sort']+queryConfig['orderBy'])[queryConfig['offset']:queryConfig['limit']]
            InmuebleSerilizer = InmueblesSerializer(inmueblesQuery, many=True)
            return Response({"count": inmeblesAll.count(), "results": InmuebleSerilizer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Error", "data": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class InmueblesDetailView(generics.RetrieveAPIView):
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
        return Response({"detail": "inmmueble eliminado con exito!!", "data": deleted[1]}, status=status.HTTP_200_OK)

class InmueblesUpdateView(views.APIView):
    def put(self, request, id):
        updateInmuebleInstance = Inmuebles.objects.get(id=id)
        # print(updateInmuebleInstance.objects)
        # return 0
        updateInmuebleSerializer = InmueblesSerializer(updateInmuebleInstance, data = updateInmuebleInstance.__dict__)
        updateInmuebleSerializer.is_valid(raise_exception=True)
        updateInmuebleSerializer.save(newData=request.data)
        return Response({"detail": "inmmueble actualizado con exito!!", "data": updateInmuebleSerializer.data}, status=status.HTTP_200_OK)