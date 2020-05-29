from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import CreateUserForm,Profile_Form
from profile_app.models import Profile,Tree_View,Matching_Income
from profile_app.models import *

from django.contrib.auth.models import User

# Create your views here.


def register(request):
	if request.method == 'POST':
		form = CreateUserForm(request.POST) 
		

		if form.is_valid():
			
			side = request.POST.get('side')
			sponsor = request.POST.get('spn')
			u_name = request.POST.get('username')


			try:
				tree_obj = Tree_View.objects.get(user_name=sponsor)
				form.save()


				b = Tree_View(user_name= u_name, left="null", right="null",left_count=0,right_count=0)
				b.save()

				m = Matching_Income(user_name=u_name)
				m.save()
				
				
				user_obj = User.objects.get(username = u_name)
				profile_obj = Profile.objects.get(user = user_obj)

				profile_obj.sponsor_id = sponsor
				profile_obj.side = side
				
				profile_obj.save()

				
				

				while True:
					if side=="Left":
						if tree_obj.left != "null":
							name = tree_obj.left
							tree_obj.left_count += 1
							tree_obj.save()
							tree_obj = Tree_View.objects.get(user_name=name)
						else:
							tree_obj.left = u_name
							tree_obj.save()
							break
					else:
						if tree_obj.right != "null":
							name = tree_obj.right
							tree_obj.right_count += 1
							tree_obj.save()
							tree_obj = Tree_View.objects.get(user_name=name)
						else:
							tree_obj.right = u_name
							tree_obj.save()
							break

				return redirect('login')

			except Exception as e:
				form = CreateUserForm()
		
	else:
		form = CreateUserForm()
		
	d = {
		'form':form,
		
	}
	return render(request, 'user_templates/register.html',d)
