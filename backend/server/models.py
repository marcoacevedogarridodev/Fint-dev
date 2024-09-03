from django.db import models


class Indicador(models.Model):
    uf = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dolar = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dolar_intercambio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    euro = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ipc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    utm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ivp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imacec = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tpm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    libra_cobre = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tasa_desempleo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bitcoin = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

