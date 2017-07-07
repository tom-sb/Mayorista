from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from cliente.models import Cliente
from inventario.models import Inventario


class Factura(models.Model):
	FORMA_PAGO= (
		('efectivo', 'Efectivo'), ('cheque', 'Cheque'),
		('tarjeta debito', 'Tarjeta debito'), ('tarjeta credito', 'Tarjeta credito'),
		('venta a credito','Venta a credito'), ('bono','Bono'),
		('vale','Vale'), ('otros','Otros'),
		)
	serie = models.IntegerField(primary_key=True, auto_created=True)#codigo de factura
	maquina = models.CharField(max_length=20)#N Seriemaquina
	fecha = models.DateField(auto_now_add=True)#fecha de Venta
	vendedor = models.ForeignKey(User)
	cliente = models.ForeignKey(Cliente)
	formaPago = models.CharField(choices=FORMA_PAGO ,
		max_length=50, verbose_name='forma de pago')
	total = models.DecimalField(max_digits=8, 
		decimal_places=2, null=True, blank=True)
	def __unicode__(self):
		return self.serie



class DetalleFactura(models.Model):
	factura =models.ForeignKey(Factura, on_delete=models.CASCADE)
	producto = models.ForeignKey(Inventario)
	descripcion = models.CharField(max_length=45)
	precio = models.DecimalField(max_digits=7, decimal_places=2)
	cantidad = models.PositiveSmallIntegerField()
	valorIva = models.DecimalField(max_digits=6, decimal_places=2)
	subtotal = models.DecimalField(max_digits=6, decimal_places=2)

	def __unicode__(self):
		return self.producto
    

