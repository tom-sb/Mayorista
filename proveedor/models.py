from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Proveedor(models.Model):
	TIPO_CUENTA = (
		('corriente', 'Corriente'),
		('ahorros', 'Ahorros'),
		('recaudo','Recaudo'),
		)
	nit = models.CharField(max_length=15, unique=True)
	nombreEmpresa = models.CharField(max_length=45)
	nombreRepresentante = models.CharField(max_length=45)
	apellidoRepresentante = models.CharField(max_length=45)
	telefonoUno = PhoneNumberField(default='+570387260001')
	telefonoDos = PhoneNumberField(default='+573040000001')
	correo = models.EmailField(max_length=100, blank=True, null=True)
	sitioWeb = models.CharField(max_length=100, blank=True, null=True)
	ciudad = models.CharField(max_length=25)
	direccion = models.CharField(max_length=45)
	banco = models.CharField(max_length=45)
	tipoCuenta = models.CharField(choices=TIPO_CUENTA ,max_length=25)
	numeroCuenta = models.CharField(max_length=15, unique=True)

	def __unicode__(self):
		return self.nombreEmpresa

