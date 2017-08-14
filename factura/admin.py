from django.contrib import admin

# Register your models here.
from .models import Factura, DetalleFactura
# Register your models here.
@admin.register(Factura)
class AdminFactura(admin.ModelAdmin):
	list_display = ( 'maquina', 'fecha', 
		'vendedor', 'cliente',)

@admin.register(DetalleFactura)
class AdminDetalleFactura(admin.ModelAdmin):
	list_display = ('factura', 'producto', 'cantidad',
		'valorIva', 'subtotal',)
