from django.test import TestCase 
from .models import Perfil
from django.contrib.auth.models import User
import pytest
# Create your tests here.

class PerfilTestCase(TestCase):
	def setUp(self):
		Perfil.object.create(numeroDocumento = "44900924",\
				telefono = "+051994184855",\
				direccion = "av. independecia sn",\
				user = User) 
