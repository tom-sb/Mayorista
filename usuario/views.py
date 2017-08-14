from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#from django.contrib.auth import logout
from .models import Perfil
from django.contrib.auth import logout
#Vistas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    UpdateView,
    CreateView,
    DeleteView
    )
from django.core.urlresolvers import reverse_lazy

#mixins
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin)


"""
def LogOut(request):
	logout(request)
	return redirect('/')
"""
def authentication(request):
    if request.method == 'POST':
        #print "metodo Post"
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if action == 'login':
            user = authenticate(username=username, password=password)
            if user is not None:
            	login(request, user)
                return redirect('usuario:system_index')
        return redirect('usuario:index')
    return render(request, 'login.html', {})


#-----------------------Perfil------------------------#
class PerfilInsert(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('usuario.add_perfil')
    model = Perfil
    success_url = reverse_lazy('usuario:system_index')
    fields = ['numeroDocumento','telefono','direccion',]
    success_url = reverse_lazy('usuario:system_index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        #form.user.groups.add('Usuario_Standard','Administrador_Centuria')
                #aca
        #user.groups.add('Usuario_Standard','Administrador_Centuria')
        return super(PerfilInsert, self).form_valid(form)


class PerfilList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ('usuario.add_perfil')
    model = Perfil
    context_object_name = 'perfiles'
#esta funcion permite ver solo las reservaciones del usuario
    def get_queryset(self):
        return Perfil.objects.filter(user=self.request.user)


#editar perfil actual
class PerfilUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('usuario.change_perfil')
    model = Perfil
    success_url = reverse_lazy('usuario:system_index')
    fields = ['numeroDocumento','telefono','direccion',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PerfilUpdate, self).form_valid(form)
#-----------------END - Profile------------------
