from django import forms
from .models import Requested_Fund,Bank_Info

class Requested_Fund_Form(forms.ModelForm):
	class Meta:
		model = Requested_Fund
		fields = ['user_name','date','fund','transection_no','proof']

class Bank_Form(forms.ModelForm):
	class Meta:
		model = Bank_Info
		fields = "__all__"