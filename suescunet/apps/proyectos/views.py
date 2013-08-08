# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from suescunet.apps.proyectos.models import mdl_proyectos
from suescunet.apps.proyectos.forms import frm_proyectos
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,InvalidPage



def view_agregar_proyecto(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			contenidoForm = frm_proyectos(request.POST,request.FILES)
			if contenidoForm.is_valid:
				contenidoForm.save()
				return HttpResponseRedirect('/proyectos/1')


		formulario = frm_proyectos()
		contexto = {'formulario':formulario}

		return render_to_response('proyectos/proyectos_ingresar.html',contexto,context_instance=RequestContext(request))


def view_proyectos(request,pagina):
	proyectos = mdl_proyectos.objects.filter(publicado=True)
	paginator  = Paginator(proyectos,10)

	try:
		page = int(pagina)
	except:
		page = 1

	try:
		proyectos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		proyectos = paginator.page(paginator.num_pages)

	contexto = {"proyectos":proyectos}
	return render_to_response("proyectos/proyectos.html",contexto,context_instance = RequestContext(request))