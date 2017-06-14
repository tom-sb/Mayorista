from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
#from recursos import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [#cambiar url logout
		url(r'^logout$', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^plataforma', TemplateView.as_view(template_name="system_index.html"), name="system_index"),
    url(r'^login/$', views.authentication, name="authentication"),
    #url(r'^login', TemplateView.as_view(template_name="login.html"), name="login"),
   # url(r'^plataforma', views.ResourceInsert.as_view(), name="plataforma"),

    #url(r'^', views.hello, name="hello"),
     #   url(r'^logout$', auth_views.logout, {'next_page': '/'}, name="logout"),
    #url(r'^login/$', views.authentication, name="authentication"),


]
