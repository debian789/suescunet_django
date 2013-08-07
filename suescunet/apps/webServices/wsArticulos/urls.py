from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('suescunet.apps.webServices.wsArticulos.views',
	url(r'^ws/articulos/$','wsArticulos_view', name = 'ws_vista_articulos'),

)


