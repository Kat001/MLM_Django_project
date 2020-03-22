from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import CreateUserForm

# Create your views here.


def register(request):
	form = CreateUserForm()
	if request.method == 'POST' or request.method is None:
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			print("success")
			username = form.cleaned_data.get('username')
			messages.success(request,'Registration successful')
			return redirect('login')
	else:
		pass

	d = {
		'form':form,
	}
	return render(request, 'user_templates/register.html',d)
