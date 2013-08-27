from django.db import models
from suescunet.apps.elementos_desarrollo.models import *

def url(self,filename):
		ruta = "ArchivosAdjuntos/archivos/%s"% filename
		return ruta

class mdl_codigos(models.Model):
	titulo 		= models.CharField(max_length=500)
	descripcion = models.TextField()
	url    		= models.URLField(max_length=300)
	so 			= models.ForeignKey(mdl_sistema_operativo) 
	lenguaje    = models.ForeignKey(mdl_lenguaje)
	archivo     = models.FileField(upload_to=url,null=True,blank=True)
	codigo 		= models.TextField()
	publicado 	= models.BooleanField(default=True)	


	class Meta:
		verbose_name = ('Codigo')
		verbose_name_plural = ('Codigos')

	def __unicode__(self):
		return self.titulo

# Create your models here.
