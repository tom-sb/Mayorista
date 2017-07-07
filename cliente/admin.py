from django.contrib import admin

# Register your models here.
from .models import Cliente
# Register your models here.
@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
	list_display = ('dni','nombre','apellidos',
		'telefono','correo',)