from django.forms import ModelForm
from suescunet.apps.codigos.models import mdl_codigos


class frm_codigos(ModelForm):
	class Meta:
			model = mdl_codigos


