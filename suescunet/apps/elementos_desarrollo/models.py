from django.db import models



class mdl_sistema_operativo(models.Model):
	nombre = models.CharField(max_length= 200)

	def __unicode__(self):
		return self.nombre


class mdl_lenguaje(models.Model):
	nombre = models.CharField(max_length = 300)

	def __unicode__(self):
		return self.nombre

class mdl_interfaz_aplicacion(models.Model):
	nombre = models.CharField(max_length = 300)

	def __unicode__(self):
		return self.nombre


class mdl_nivel_desarrollo(models.Model):
	nombre = models.CharField(max_length= 200)

	def __unicode__(self):
		return self.nombre


#class nueva(models.Model):
#	so = models.ForeignKey(mdl_sistema_operativo)
#	nombre = models.CharField(max_length=100)


# Create your models here.
