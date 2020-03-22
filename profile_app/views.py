from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def p_user(request):
	return render(request,'profile_templates/profile.html')
