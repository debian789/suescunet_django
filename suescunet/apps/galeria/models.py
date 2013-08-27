from django.db import models

def url(self,filename):
		ruta = "MultimediaData/productos/%s"% filename
		return ruta

class galeria_model(models.Model):
	titulo = models.CharField(max_length = 200)
	contenido = models.TextField()
	publicado = models.BooleanField(default=True)
	fecha_publicado = models.DateField(auto_now = True)
	imagen = models.ImageField(upload_to=url,null=True,blank=True)
	precio = models.DecimalField(max_digits=6,decimal_places=2)
	stock = models.IntegerField()

	class Meta:
		verbose_name = ('Galeria')
		verbose_name_plural = ('Galerias')

	
	def __unicode__(self):
		return self.titulo
 

	

# Create your models here.
