from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Perfil - Relacion con users
class Perfil(models.Model):
	numeroDocumento = models.CharField(max_length=15, unique=True)
	telefono = PhoneNumberField(default='+573040000000')
	direccion = models.CharField(max_length=45)
	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.username

