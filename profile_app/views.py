from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import Requested_Fund_Form
from .models import Requested_Fund
from .models import Fund,Profile

from django.contrib.auth.models import User


# Create your views here.


@login_required
def p_user(request):
	return render(request,'profile_templates/profile.html')

@login_required
def fund_request(request):
	form = Requested_Fund_Form()
	rqs =  Requested_Fund.objects.all
	if request.method=='POST' or request.method is None:
		form = Requested_Fund_Form(request.POST)
		if form.is_valid:
			form.save()
			return redirect('fund_request')

	else:
		form = Requested_Fund_Form()

	d = {
	  'form' : form,
	  'rqs' : rqs,
	  
	}
	return render(request,'profile_templates/request_fund.html',d)

def activate_id(request):
	user_obj = request.user
	fund_obj = Fund.objects.get(user = user_obj)
	profile_obj = Profile.objects.get(user = user_obj)
	#user_obj = User.objects.get(username= u_name)

	avail_fund = fund_obj.avail_fund
	
	if request.method=='POST':
		price = request.POST.get('price1')
		u_name = request.POST.get('u__name')



		#user_obj = User.objects.get(username= u_name)
		#fund_obj = Fund.objects.get(user = user_obj)
		#profile_obj = Profile.objects.get(user = user_obj)

			#print(user_obj.username,fund_obj.avail_fund,profile_obj.is_active)

		if profile_obj.is_active:
			profile_obj.active_amount += int(price)
			fund_obj.avail_fund -= int(price)
			print("donnn")
		else:
			profile_obj.is_active = True
			profile_obj.active_amount = int(price)
			fund_obj.avail_fund -= int(price)
			print("doone")
					


		profile_obj.save()
		fund_obj.save()

		avail_fund = fund_obj.avail_fund
				
	
	
	
	d = {
		'fund' : avail_fund,
	}



	return render(request,'profile_templates/activate_id.html',d)




def activateother_id(request):
	current_user_obj = request.user
	fund_obj = Fund.objects.get(user = current_user_obj)
	avail_fund = fund_obj.avail_fund


	if request.method=='POST':
		price = request.POST.get('price1')
		target_username = request.POST.get('u_name')
		target_username1 = request.POST.get('u_name1')

		print(target_username1,target_username1,price)
		print(current_user_obj.username)
		print(avail_fund)

		user_obj = User.objects.get(username= target_username)
		profile_obj = Profile.objects.get(user = user_obj)

		if target_username == target_username1:
			if profile_obj.is_active:
				profile_obj.active_amount += int(price)
				fund_obj.avail_fund -= int(price)
			else:
				profile_obj.is_active = True
				profile_obj.active_amount = int(price)
				fund_obj.avail_fund -= int(price) 
		profile_obj.save()
		fund_obj.save()

		avail_fund = fund_obj.avail_fund
				
	
	
	
	d = {
		'fund' : avail_fund,
	}			



	return render(request,'profile_templates/activate_other_id.html',d)

