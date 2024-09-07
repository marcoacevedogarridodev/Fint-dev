from rest_framework import serializers
from django.contrib.auth.models import User
from server.models import Indicador 
from rest_framework import viewsets


class IndicadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicador
        fields = ['dolar', 'dolar_intercambio', 'euro', 'ipc', 'utm', 'ivp', 'imacec', 'tpm', 'libra_cobre', 'tasa_desempleo', 'bitcoin']


class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer
