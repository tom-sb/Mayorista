from django.test import TestCase
from proveedor.models import Proveedor
import pytest

# Create your tests here

class TestProveedor(TestCase):
	def setUp(self):
		Proveedor.objects.create(nit = "123456",\
				nombreEmpresa = "proveedor1.SAC",\
				nombreRepresentante = "Mark",\
				apellidoRepresentante = "Zuckerberg",\
				telefonoUno = "+51994788744",\
				telefonoDos = "+51623443",\
				correo = "mark@facebook.com",\
				sitioWeb = "facebook.com",\
				ciudad = "PaloAlto",\
				direccion = "av. venezuela sn",\
				banco = "bcp",\
				tipoCuenta = "corriente",\
				numeroCuenta = "215-3244-432")
	def testDataBase(self):
		all_database = Proveedor.objects.all()
		assert len(all_database) == 1
