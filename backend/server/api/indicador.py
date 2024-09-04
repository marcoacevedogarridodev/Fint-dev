from rest_framework import serializers, viewsets
from server.models import Indicador
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from server.permissions import IsOwnerOrReadOnly


class IndicadorSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Indicador
        fields = "__all__"


class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializers


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

