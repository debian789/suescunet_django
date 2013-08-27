# Create your views here.
from django.http import HttpResponse
from suescunet.apps.galeria.models import galeria_model
# integramos la serializacion de los objetos


from django.core import serializers

def wsGalerias_view(request):
	datos = serializers.serialize("json",galeria_model.objects.filter(publicado=True))
	#retorna la informacion en forma json 
	return HttpResponse(datos,mimetype="application/json")

