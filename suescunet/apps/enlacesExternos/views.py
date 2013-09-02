from suescunet.apps.enlacesExternos.models import enlacesExterno_model
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.template import RequestContext
from django.shortcuts import render_to_response


def view_enlaces (request,pagina):
	enlaces = enlacesExterno_model.objects.filter(publicado=True)
	paginator = Paginator(enlaces,10)

	try:
		page = int(pagina)
	except:
		page = 1

	try:
		enlaces = paginator.page(page)
	except (EmptyPage,InvalidPage):
		proyectos = paginator.page(paginator.num_pages)

	contexto = {"enlaces":enlaces}
	return render_to_response("enlaces/enlaces.html",contexto,context_instance = RequestContext(request))


# Create your views here.
