from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('suescunet.apps.fragmentos.views',
	url(r'^fragmentos/(?P<pagina>.*)/$','view_fragmentos', name = 'view_fragmentos'),
	url(r'^add/fragmento/$','view_agregar_fragmento', name = 'agregar_fragmento'),
	#url(r'^add/articulo2/$','add_articulos_view2', name = 'vista_articulo_ingresar2'),
	#url(r'^articulo/(?P<id_articulo>.*)/$','single_articulo_view', name = 'vista_articulo'),

)




