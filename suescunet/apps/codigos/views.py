# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from suescunet.apps.codigos.models import mdl_codigos
from suescunet.apps.codigos.forms import frm_codigos
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,InvalidPage



def view_agregar_codigo(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			contenidoForm = frm_codigos(request.POST,request.FILES)
			if contenidoForm.is_valid:
				contenidoForm.save()
				return HttpResponseRedirect('/codigos/1')


		formulario = frm_codigos()
		contexto = {'formulario':formulario}
	

		return render_to_response('codigos/codigo_ingresar.html',contexto,context_instance=RequestContext(request))


def view_codigos(request,pagina):
	codigos = mdl_codigos.objects.filter(publicado=True)
	paginator  = Paginator(codigos,10)

	for x in codigos:
		print x

	try:
		page = int(pagina)
	except:
		page = 1

	try:
		codigos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		codigos = paginator.page(paginator.num_pages)

	contexto = {"codigos":codigos}
	return render_to_response("codigos/codigos.html",contexto,context_instance = RequestContext(request))