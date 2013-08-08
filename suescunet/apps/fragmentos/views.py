# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from suescunet.apps.fragmentos.models import mdl_fragmentos
from suescunet.apps.fragmentos.forms import frm_fragmentos
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,InvalidPage



def view_agregar_fragmento(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			contenidoForm = frm_fragmentos(request.POST,request.FILES)
			if contenidoForm.is_valid:
				contenidoForm.save()
				return HttpResponseRedirect('/fragmentos/1')


		formulario = frm_fragmentos()
		contexto = {'formulario':formulario}

		return render_to_response('fragmentos/fragmento_ingresar.html',contexto,context_instance=RequestContext(request))


def view_fragmentos(request,pagina):
	fragmentos = mdl_fragmentos.objects.filter(publicado=True)
	paginator  = Paginator(fragmentos,10)

	try:
		page = int(pagina)
	except:
		page = 1

	try:
		fragmentos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		fragmentos = paginator.page(paginator.num_pages)

	contexto = {"fragmentos":fragmentos}
	return render_to_response("fragmentos/fragmentos.html",contexto,context_instance = RequestContext(request))