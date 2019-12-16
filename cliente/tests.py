from django.test import TestCase
from cliente.models import Cliente
import pytest
# Create your tests here.
class BasicTest(TestCase):
    def test_fields(self):
        Cliente.objects.create( dni="71457216", \ 
            nombre="Javier",apellidos="Obando", \
            correo="adf@unsa.edu",ciudad="Toquepala",\
            direccion="av las orquideas",banco="bcp",\
            )
    def testdatabase(self):
        all_database=Cliente.objects.all()
        assert len(all_database) == 1
