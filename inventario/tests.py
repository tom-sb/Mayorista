from django.test import TestCase
from inventario.models import Inventario
import pytest
# Create your tests here.

#testInventario
class TestInventario(TestCase):
    def setUp(self):
        Inventario.objects.create(Codigo = "123456",\
                elemento = "arroz",cantidad = 12, \
                descripcion = "arroz de alta calidad",\
                valorCompra = 234,valorIva = 16,\
                valorVenta = 18)
        #self.testIn=In

    def testdatabase(self):
        all_database=Inventario.objects.all()
        assert len(all_database) == 1

    def testpreciototal(self):
        all_d=Inventario.objects.all()
        only_d=all_d[0]
        assert only_d.preciototal() == 12*234
