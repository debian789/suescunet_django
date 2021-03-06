from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^',include('suescunet.apps.galeria.urls')),
	url(r'^',include('suescunet.apps.home.urls')),
    url(r'^',include('suescunet.apps.webServices.wsGalerias.urls')),
    url(r'^',include('suescunet.apps.codigos.urls')),
    url(r'^',include('suescunet.apps.proyectos.urls')),
    url(r'^',include('suescunet.apps.enlacesExternos.urls')),
    


	url(r'^media/(?P<path>.*)$','django.views.static.serve',{"document_root":settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{"document_root":settings.STATICFILES_DIRS}),

    # url(r'^$', 'suescunet.views.home', name='home'),
    # url(r'^suescunet/', include('suescunet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
