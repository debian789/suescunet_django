from django import forms


class loginForm(forms.Form):
	userName = forms.CharField(label="",widget=forms.TextInput(
		attrs={'class': 'input',
			   'placeholder':'Usuario'
			   }))
	password = forms.CharField(label="",widget=forms.PasswordInput(render_value=False,attrs={'placeholder':'Password'}))

	#cass# Meta:
		#widget = { "userName":}