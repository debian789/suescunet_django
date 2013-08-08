from django.forms import ModelForm
from suescunet.apps.fragmentos.models import mdl_fragmentos


class frm_fragmentos(ModelForm):
	class Meta:
			model = mdl_fragmentos


