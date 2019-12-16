from django.test import TestCase,RequestFactory
from factura.models import Factura
from .views import factura_detail
import pytest
# Create your tests here.

class TestFactura(TestCase):
    def setUp(self):

        vendedor=Vendedor()
        cliente=cliente()
        self.Fact = Factura.objects.create(maquina = 'MN323',\
                vendedor=vendedor, cliente=cliente, \
                formaPago = 'efectivo', iva= 123,total = 324,)


    def testmaquina(self):
        assert Factura.objects.get(pk=self.Fact.pk).maquina == 'MN323'
