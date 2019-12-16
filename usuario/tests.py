from django.test 
from .models import Perfil
from django.contrib.auth.models import User

class PerfilTestCase(TestCase):
	def setUp(self):
		Perfil(numeroDocumento = '44900924', telefono = '+051994184855', direccion = 'av. independecia sn', user = models.OneToOneField(User)
        
# Create your tests here.
