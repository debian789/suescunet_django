from django.shortcuts import render_to_response #arma el contenido 
from django.template import RequestContext # permite incluir el contexto
from suescunet.apps.articulos.models import articulos_model # modelos
from suescunet.apps.articulos.forms import addArticulosForms,addArticulosForms2 # Formularios
from django.http import HttpResponseRedirect #Redireccionar
from django.core.paginator import Paginator,EmptyPage,InvalidPage #pagina django



######## formularios  ###############

def add_articulos_view1(request):
	info = "Inicializado"		
	if request.user.is_authenticated():

		if request.method == "POST":
			formulario = addArticulosForms2(request.POST,request.FILES) #FILES agrega los archivos gargados
			if formulario.is_valid():

				titulo = formulario.cleaned_data['titulo']
				contenido = formulario.cleaned_data['contenido']
				publicado = formulario.cleaned_data['publicado']
				imagen = formulario.cleaned_data['imagen'] 

				articulo= articulos_model()
				articulo.titulo = titulo
				articulo.contenido = contenido
				articulo.publicado = publicado 
				if imagen:
					articulo.imagen = imagen 

				articulo.save()

				#formulario.save()
			return HttpResponseRedirect('/articulos/page/1')

		else:

			formulario = addArticulosForms2()
			contexto = {"formulario":formulario}
			return render_to_response("articulos/articulos_ingresar.html",contexto, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/")



def add_articulos_view2(request):
	if request.user.is_authenticated():

		if request.method == "POST":
			contenidoForm = addArticulosForms(request.POST,request.FILES)
			if contenidoForm.is_valid :
				contenidoForm.save()
				return HttpResponseRedirect('/articulos/page/1')

		
		formulario = addArticulosForms()
		contexto = {'formulario':formulario}

		return render_to_response('articulos/articulos_ingresar.html',contexto,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/")

######### fin de formularios #############
#### vistas ########


def articulo_view(request,pagina):
	articulos = articulos_model.objects.filter(publicado=True)
	paginator = Paginator(articulos,50) #cuantos productos quires por pagina

	try:
			page = int(pagina)
	except:
		page = 1

	try:
		articulos = paginator.page(page)
	except (Emptypage,InvalidPage):
		articulos = paginator.page(paginator.num_pages)


	contexto =  {"articulos":articulos}
	return render_to_response("articulos/articulos.html",contexto,context_instance=RequestContext(request))


def single_articulo_view(request,id_articulo):
	articulo = articulos_model.objects.get(id=id_articulo)
	contexto = {'articulos':articulo}
	return render_to_response('articulos/articulo.html',contexto,context_instance=RequestContext(request))




#	return render_to_response("articulos/articulos.html",context_instance=RequestContext(request))	
