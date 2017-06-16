from django.shortcuts import render, redirect,get_object_or_404

from .models import Proveedor
#importar http
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
#Vistas 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    UpdateView, 
    CreateView, 
    DeleteView
    )
from django.core.urlresolvers import reverse_lazy


#---------------------Proveedor ---------------------------------
class ProveedorInsert(CreateView):
	permission_required = ('proveedor: add_proveedor')
	model = Proveedor
	success_url = reverse_lazy ('usuario:system_index')
	fields = ['nit','nombreEmpresa','nombreRepresentante',
	'apellidoRepresentante','telefonoUno','telefonoDos',
	'correo','sitioWeb','ciudad','direccion','banco',
	'tipoCuenta','numeroCuenta',]
	
class ProovedorList(ListView):#, 
#    PermissionAdminRequiredMixin, PermissionStandardRequiredMixin):
    model = Proveedor
    context_object_name = 'proveedores'

class ProveedorUpdate(UpdateView):
	model = Proveedor
	success_url = reverse_lazy('proveedor:proveedor_list')
	fields = ['nit','nombreEmpresa','nombreRepresentante',
	'apellidoRepresentante','telefonoUno','telefonoDos',
	'correo','sitioWeb','ciudad','direccion','banco',
	'tipoCuenta','numeroCuenta',]


def proveedor_detail(request, pk):
    #capturar id de reservaciones
    proveedor = get_object_or_404(Proveedor, pk=pk)
    #hacer iterable la relacion ManyToMany con el all
    #resources = reservation.resource.all()
    template = loader.get_template('proveedor/proveedor_detail.html')
    context = {
        'proveedor' : proveedor
    }
    return HttpResponse(template.render(context, request))
