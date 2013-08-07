from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('suescunet.apps.articulos.views',
	url(r'^articulos/page/(?P<pagina>.*)/$','articulo_view', name = 'vista_articulos'),
	url(r'^add/articulo1/$','add_articulos_view1', name = 'vista_articulo_ingresar1'),
	url(r'^add/articulo2/$','add_articulos_view2', name = 'vista_articulo_ingresar2'),
	url(r'^articulo/(?P<id_articulo>.*)/$','single_articulo_view', name = 'vista_articulo'),

)






