from django.db import models
from suescunet.apps.elementos_desarrollo.models import *

def url(self,filename):
		ruta = "ArchivosAdjuntos/archivos/%s"% filename
		return ruta

class mdl_fragmentos(models.Model):
	nombre 		= models.CharField(max_length=500)
	descripcion = models.TextField()
	url    		= models.URLField(max_length=300)
	so 			= models.ForeignKey(mdl_sistema_operativo) 
	lenguaje    = models.ForeignKey(mdl_lenguaje)
	archivo     = models.FileField(upload_to=url,null=True,blank=True)
	publicado 	= models.BooleanField(default=True)	

	def __unicode__(self):
		return self.nombre

# Create your models here.
