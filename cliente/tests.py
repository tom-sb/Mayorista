from django.test import TestCase

# Create your tests here.
class BasicTest(TestCase):
	def test_fields(self):
		item = Item()
		item.TIPO_CUENTA = "Make more cuentas"
		item.nombre = "here name"
		item.save()
		item = Item.objects.all()
		self.assertEquals(item.count(), 1)

		record = Item.objects.get(pk1)
		self.assertEqual(record, item)
    
