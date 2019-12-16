from django.test import TestCase 
from usuario.models import Perfil
from django.contrib.auth.models import User
import pytest
# Create your tests here.

class PerfilTestCase(TestCase):
	def setUp(self):
		Perfil.objects.create(numeroDocumento = "44900924",\
				telefono = "+051994184855",\
				direccion = "av. independecia sn",\
				user = User) 
	
	def testDataBase(self):
		all_database = Perfil.objects.all()
		assert len(all_database) == 1
