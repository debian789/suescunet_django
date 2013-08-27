from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('suescunet.apps.webServices.wsGalerias.views',
	url(r'^ws/Galerias/$','wsGalerias_view', name = 'ws_vista_galerias'),

)


