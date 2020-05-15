from django import forms
from .models import Requested_Fund

class Requested_Fund_Form(forms.ModelForm):
	class Meta:
		model = Requested_Fund
		fields = ['user_name','date','fund','transection_no','proof']