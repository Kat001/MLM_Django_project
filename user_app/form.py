from django import forms
from profile_app.models import Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
	email = forms.EmailField()
	
	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'email', 'password1', 'password2']:
			self.fields[fieldname].help_text = None



	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class Profile_Form(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Profile_Form, self).__init__(*args, **kwargs)
		for fieldname in ['sponsor_id','side']:
			self.fields[fieldname].help_text = None

	class Meta:
		model = Profile
		fields = ['sponsor_id','side']

