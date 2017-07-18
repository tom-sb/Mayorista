from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.
from .models import Inventario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    UpdateView,
    CreateView,
    DeleteView
    )
from django.core.urlresolvers import reverse_lazy


class InventarioInsert(CreateView):
	permission_required = ('inventario.add_inventario')
	model = Inventario
	success_url = reverse_lazy('inventario:inventario_list')
	fields = ['codigo', 'elemento', 'cantidad', 'descripcion',
	 'valorCompra', ]
	"""
	def calcular_precio_venta(self, form):
		print (valorCompra)
		form.instance.elemento = "platico"
	 	form.instance.valorVenta = 200
	 	return super(InventarioInsert, self).calcular_precio_venta(form)

	 	"""


class InventarioList(ListView):
	model = Inventario
	context_object_name = 'elementos'

class InventarioUpdate(UpdateView):
	model = Inventario
	success_url = reverse_lazy('inventario:inventario_list')
	fields = ['codigo', 'elemento', 'cantidad', 'descripcion',
            'valorCompra', 'valorIva', 'valorVenta']
    
class InventarioDelete(DeleteView):#,
#    PermissionAdminRequiredMixin, PermissionStandardRequiredMixin):
	permission_required= ('inventario.delete_inventario')
	model = Inventario
	success_url = reverse_lazy('inventario:inventario_list')



def inventario_detail(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    template = loader.get_template('inventario/inventario_detail.html')
    context = {
        'inventario' : inventario
    }
    return HttpResponse(template.render(context, request))
