from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('suescunet.apps.codigos.views',
	url(r'^codigos/(?P<pagina>.*)/$','view_codigos', name = 'view_codigos'),
	url(r'^add/codigo/$','view_agregar_codigo', name = 'agregar_codigo'),
	#url(r'^add/articulo2/$','add_articulos_view2', name = 'vista_articulo_ingresar2'),
	#url(r'^articulo/(?P<id_articulo>.*)/$','single_articulo_view', name = 'vista_articulo'),

)




