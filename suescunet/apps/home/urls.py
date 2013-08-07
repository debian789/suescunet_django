from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('suescunet.apps.home.views',
	url(r'^logout/$','logout_view',name="vista_logout"),
	url(r'^login/$','login_view',name="vista_login"),
	url(r'^$','index_view',name="index"),
	)