from django.test import TestCase

# Create your tests here.
class BasicTest(TestCase):
    def test_fields(self):
        cliente = Cliente()
        cliente.TIPO_CUENTA = "Make more cuentas"
        cliente.nombre = "here name"
        cliente.save()
"""      item = Item,objects.all()
        self.assertEquals(item.count(), 1)"""
        record = Cliente.objects.get(pk1)
        self.assertEqual(record, item)
    
