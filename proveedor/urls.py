from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
#from recursos import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [#cambiar url logout
	url(r'^proveedor/new', views.ProveedorInsert.as_view(),
	name="proveedor_insert"),
	url(r'^proveedor/list$', views.ProovedorList.as_view(),
		name='proveedor_list'),
	url(r'^proveedor/(?P<pk>[0-9]+)/$', views.proveedor_detail, 
    	name="proveedor_detail"),
	url(r'^proveedor/edit(?P<pk>[0-9]+)/$',views.ProveedorUpdate.as_view(),
		name='proveedor_edit'),
	url(r'^proveedor/buscar$', views.BuscarView.as_view(), name='buscar'),



]
