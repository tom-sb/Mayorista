from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Cliente
from django.views.generic.edit import (
	UpdateView,
	CreateView, 
    DeleteView
	)
from django.core.urlresolvers import reverse_lazy


class ClienteInsert(CreateView):
	permission_required = ('cliente.add_cliente')
	model = Cliente 
	success_url = reverse_lazy('cliente:cliente_list')
	fields = ['dni', 'nombre', 'apellidos', 'telefono',
		'correo', 'ciudad', 'direccion', 'banco',
		'tipoCuenta', 'numeroCuenta', ]
	#succes_url = reverse_lazy('cliente:cliente_list')


class ClienteList(ListView):
	model = Cliente
	context_object_name = 'clientes'


class ClienteUpdate(UpdateView):
	model = Cliente
	success_url = reverse_lazy('cliente:cliente_list')
	fields = ['dni', 'nombre', 'apellidos', 'telefono',
		'correo', 'ciudad', 'direccion', 'banco',
		'tipoCuenta', 'numeroCuenta', ]


class ClienteDelete(DeleteView):
	permission_required = ('clinete.delete_cliente')
	model = Cliente
	success_url = reverse_lazy('cliente:cliente_list')


def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    template = loader.get_template('cliente/cliente_detail.html')
    context = {
        'cliente' : cliente
    }
    return HttpResponse(template.render(context, request))