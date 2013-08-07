#from django import forms
from django.forms import ModelForm
from suescunet.apps.articulos.models import articulos_model
from django import forms

class addArticulosForms(ModelForm):
	class Meta:
		model = articulos_model


class addArticulosForms2(forms.Form):
	titulo = forms.CharField(max_length = 200)
	contenido = forms.CharField(widget=forms.Textarea)
	publicado = forms.BooleanField(required=True)
	imagen = forms.ImageField(required=False)
	#fecha_publicado = forms.DateField(auto_now = True)