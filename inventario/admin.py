from django.contrib import admin

from .models import Inventario
# Register your models here.
@admin.register(Inventario)
class AdminInventario(admin.ModelAdmin):
	list_display = ('codigo', 'elemento', 'cantidad', 
		'descripcion', 'valorCompra', 'valorIva',
		'valorVenta',)
