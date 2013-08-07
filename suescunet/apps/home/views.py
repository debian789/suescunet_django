from django.shortcuts import render_to_response
from django.template import RequestContext
from suescunet.apps.home.forms import loginForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect



def login_view(request):
	mensaje=""
	if request.user.is_authenticated():
		return HttpResponseRedirect("/")
	else:
		if request.method == "POST":
			form = loginForm(request.POST)
			if form.is_valid():
				username=form.cleaned_data['userName']
				password= form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o password incorrectos"
		form = loginForm()
		contexto = {'form':form,'mensaje':mensaje}
		print mensaje
		return render_to_response('home/login.html',contexto, context_instance=RequestContext(request))


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))
