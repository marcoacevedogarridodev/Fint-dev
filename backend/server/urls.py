from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from server.api.indicador import IndicadorViewSet

router = routers.DefaultRouter()
router.register(r'indicadores', IndicadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
