from django.test import TestCase

# Create your tests here.
class BasicTest(TestCase):
    def test_fields(self):
        cliente = Cliente()
        cliente.TIPO_CUENTA = "Make more cuentas"
        cliente.nombre = "here name"
        cliente.save()
        record = Cliente.objects.get(pk1)
        self.assertEqual(record, item)
    
