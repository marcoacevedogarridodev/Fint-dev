from __future__ import absolute_import, unicode_literals

# Hacer que Celery cargue automáticamente las tareas de los módulos de la aplicación
from .celery import app as celery_app

__all__ = ('celery_app',)