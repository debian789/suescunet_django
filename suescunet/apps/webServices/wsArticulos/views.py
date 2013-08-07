# Create your views here.
from django.http import HttpResponse
from suescunet.apps.articulos.models import articulos_model
# integramos la serializacion de los objetos


from django.core import serializers

def wsArticulos_view(request):
	datos = serializers.serialize("json",articulos_model.objects.filter(publicado=True))
	#retorna la informacion en forma json 
	return HttpResponse(datos,mimetype="application/json")

