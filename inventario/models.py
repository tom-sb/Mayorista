from __future__ import unicode_literals
from django.db.models import signals
from django.db import models
from proveedor.models import Proveedor
import decimal

TAX_VALUE = 0.18
GANANCIA = 1.40

class Inventario(models.Model):
	codigo = models.CharField(max_length=25, unique=True)
	elemento = models.CharField(max_length=25, unique=True)
	cantidad = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length=45)
	valorCompra = models.DecimalField(max_digits=7,
		decimal_places=2, default=0.00)
	valorIva = models.DecimalField(max_digits=6,
		decimal_places=2, default=0.00)
	valorVenta = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

	def __unicode__(self):
		return self.elemento

	def preciototal(self):
		precioTotal = self.valorCompra*self.cantidad
		return precioTotal


	def save(self, *args, **kwargs):
		if self.valorCompra:
			self.valorVenta = round(float(self.valorCompra)* GANANCIA, 3)
			self.valorIva = round(float(self.valorVenta) * TAX_VALUE, 3)
			super(Inventario, self).save(*args, **kwargs)
		else:
			self.valorIva=0
			super(Inventario, self).save(*args, **kwargs)


