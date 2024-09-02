from django.db import models


class Indicador(models.Model):
    uf = models.DecimalField(max_digits=10, decimal_places=2)

 

