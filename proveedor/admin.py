from django.contrib import admin

from .models import Proveedor
# Register your models here.
@admin.register(Proveedor)
class AdminProovedor(admin.ModelAdmin):
	list_display = ('nit','nombreEmpresa','ciudad',
		'direccion','banco','tipoCuenta','numeroCuenta',)