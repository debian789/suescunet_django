from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('suescunet.apps.enlacesExternos.views',
	url(r'^enlaces/(?P<pagina>.*)/$','view_enlaces', name = 'view_enlaces'),
	#url(r'^add/enlace/$','view_agregar_proyecto', name = 'agregar_proyecto'),
	#url(r'^add/articulo2/$','add_articulos_view2', name = 'vista_articulo_ingresar2'),
	#url(r'^articulo/(?P<id_articulo>.*)/$','single_articulo_view', name = 'vista_articulo'),

)



