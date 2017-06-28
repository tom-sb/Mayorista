from __future__ import unicode_literals

from django.db import models
from proveedor.models import Proveedor
from inventario.models import Inventario
"""
class Compras(models.Model):
	codigo = models.CharField(max_length=30)
	fecha = models.DateField(auto_now_add=False)
	proveedor = models.ForeignKey(Proveedor)
	elemento = models.ForeignKey(Inventario)
	cantidad = models.PositiveSmallIntegerField()
	valorCompra = models.DecimalField(max_digits=7,
		decimal_places=2, default=0.00)

no usar many to many hacerlo con puro foreing y tener un identificado de muchos

"""


