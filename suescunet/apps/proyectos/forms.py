

from django.forms import ModelForm
from suescunet.apps.proyectos.models import mdl_proyectos


class frm_proyectos(ModelForm):
	class Meta:
			model = mdl_proyectos


