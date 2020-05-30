from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import Requested_Fund_Form,Bank_Form
from .models import Requested_Fund
from .models import Fund,Profile,Tree_View,All_Matching_Income
from .models import *

from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


@login_required
def p_user(request):
	user = request.user
	profile_obj = Profile.objects.get(user = user)
	binary_obj  = Binary_Wallet.objects.get(user=user)
	direct_obj = Direct_Wallet.objects.get(user=user)
	roi_obj  = Roi_Wallet.objects.get(user=user)

	amount = binary_obj.b_income + direct_obj.d_income + roi_obj.r_income

	#print(user1)

	d = {
	'user' : user,
	'profile_obj' : profile_obj,
	'binary_obj' : binary_obj,
	'direct_obj' : direct_obj,
	'roi_obj'  : roi_obj,
	'amount'   : amount,
	}
	return render(request,'profile_templates/profile.html',d)

def user_profile(request):
	user = request.user
	profile_obj = Profile.objects.get(user = user)
	d = {
		'user' : user,
		'profile_obj' : profile_obj,
	}
	return render(request,'profile_templates/user_profile.html',d)

def update_profile(request):
	return render(request,'profile_templates/update_profile.html')

@login_required
def fund_request(request):
	user = request.user
	name1 = user.username
	try:
		form = Requested_Fund_Form()
		rqs =  Requested_Fund.objects.filter(user_name=name1)

		if request.method=='POST' or request.method is None:
			form = Requested_Fund_Form(request.POST)
			if form.is_valid:
				form.save()
				#messages.success(request,f'Successfully Done!')
				return redirect('fund_request')

		else:
			form = Requested_Fund_Form()
	except Exception as e:
		return redirect('fund_request')

	d = {
	  'form' : form,
	  'rqs' : rqs,
	  'c' : 1,
	  
	}
	return render(request,'profile_templates/request_fund.html',d)

def activate_id(request):
	user_obj = request.user
	fund_obj = Fund.objects.get(user = user_obj)
	profile_obj = Profile.objects.get(user = user_obj)
	

	avail_fund = fund_obj.avail_fund


	try:
		if request.method=='POST':
			price = request.POST.get('price1')
			u_name = request.POST.get('u__name')


			if profile_obj.is_active:
				profile_obj.active_amount += int(price)
				fund_obj.avail_fund -= int(price)

			else:
				profile_obj.is_active = True
				profile_obj.active_amount = int(price)
				fund_obj.avail_fund -= int(price)

			fund_obj.save()

			
			R = Update_ROI(user = user_obj,activated_amount=price,ending_date='1999-12-20')
			R.save()

			sponsor = profile_obj.sponsor_id
			name11 = user_obj.username
			user_obj = User.objects.get(username=sponsor)
			profile_obj = Profile.objects.get(user=user_obj)
			if profile_obj.is_active:
				income = (int(price) * 10)/100
				D = DirectSponsor_Income(user=user_obj,user_name=name11,
										 activated_amount=price,direct_income=income)

				D.save()

				d_obj = Direct_Wallet.objects.get(user = user_obj)
				d_obj.d_income += income
				d_obj.total_dincome += income
				d_obj.save()

				profile_obj.save()
				

				
				
	except Exception as e:
		return redirect('activate_id')
				

			
						


					
	
	
	
	d = {
		'fund' : avail_fund,
	}



	return render(request,'profile_templates/activate_id.html',d)




def activateother_id(request):
	current_user_obj = request.user
	fund_obj = Fund.objects.get(user = current_user_obj)
	
	avail_fund = fund_obj.avail_fund

	try:
		if request.method=='POST':
			price = request.POST.get('price1')
			target_username = request.POST.get('u_name')
			target_username1 = request.POST.get('u_name1')

			

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

				fund_obj.save()

				R = Update_ROI(user = user_obj,activated_amount=price,ending_date='1999-12-20')
				R.save()
				profile_obj.save()
				

				

				sponsor = profile_obj.sponsor_id
				user_obj = User.objects.get(username=sponsor)
				profile_obj = Profile.objects.get(user=user_obj)

				if profile_obj.is_active:
					income = (int(price) * 10)/100
					D = DirectSponsor_Income(user=user_obj,user_name=target_username,
										 activated_amount=price,direct_income=income)
					D.save()	
					
					d_obj = Direct_Wallet.objects.get(user = user_obj)
					d_obj.d_income += income
					d_obj.total_dincome += income
					d_obj.save()
	except Exception as e:
		return redirect('activate_other_id')				
	
	d = {
		'fund' : avail_fund,
	}			



	return render(request,'profile_templates/activate_other_id.html',d)

@login_required
def leftside_info(request):
	l = []
	current_user_obj = request.user
	u_name = current_user_obj.username
	profile_obj = Profile.objects.get(user = current_user_obj)
	tree_view_obj = Tree_View.objects.get(user_name=u_name)


	if tree_view_obj.left != "null":
		u_name = tree_view_obj.left
		tree_view_obj = Tree_View.objects.get(user_name=u_name)

		current_user_obj = User.objects.get(username = u_name)
		profile_obj = Profile.objects.get(user = current_user_obj)

		
		stack = [tree_view_obj]

		l = [[tree_view_obj,profile_obj]]
		
		while len(stack)>0:
			a = []
			item = stack.pop()
			#print(item.user_name,item.left,item.right)

			if item.left != "null":
				name = item.left
				item1 = Tree_View.objects.get(user_name=name)

				current_user_obj = User.objects.get(username=name)
				profile_obj = Profile.objects.get(user=current_user_obj)
				a.append(item1)
				a.append(profile_obj)

				l.append(a)
				a = []
				stack.append(item1)

			if item.right != "null":
				name = item.right
				item2 = Tree_View.objects.get(user_name=name)

				current_user_obj = User.objects.get(username=name)
				profile_obj = Profile.objects.get(user=current_user_obj)
				a.append(item2)
				a.append(profile_obj)

				l.append(a)
				stack.append(item2)
	else:
		pass

	



	
	d = {
		'l' : l,
		'null' : "null",
	}

	return render(request,'profile_templates/leftside_info.html',d)



def rightside_info(request):
	l=[]
	current_user_obj = request.user
	u_name = current_user_obj.username
	profile_obj = Profile.objects.get(user = current_user_obj)
	tree_view_obj = Tree_View.objects.get(user_name=u_name)

	if tree_view_obj.right != 'null':
		u_name = tree_view_obj.right
		tree_view_obj = Tree_View.objects.get(user_name=u_name)

		current_user_obj = User.objects.get(username = u_name)
		profile_obj = Profile.objects.get(user = current_user_obj)

		
		stack = [tree_view_obj]

		l = [[tree_view_obj,profile_obj]]
		
		while len(stack)>0:
			a = []
			item = stack.pop()
			#print(item.user_name,item.left,item.right)

			if item.left != "null":
				name = item.left
				item1 = Tree_View.objects.get(user_name=name)

				current_user_obj = User.objects.get(username=name)
				profile_obj = Profile.objects.get(user=current_user_obj)
				a.append(item1)
				a.append(profile_obj)

				l.append(a)
				a = []
				stack.append(item1)

			if item.right != "null":
				name = item.right
				item2 = Tree_View.objects.get(user_name=name)

				current_user_obj = User.objects.get(username=name)
				profile_obj = Profile.objects.get(user=current_user_obj)
				a.append(item2)
				a.append(profile_obj)

				l.append(a)
				stack.append(item2)
	else:
		pass
	
	
	d = {
		'l' : l,
		'null' : "null",
	}

	return render(request,'profile_templates/rightside_info.html',d)



def myleft_referral(request):
	l = []
	current_user_obj = request.user
	name = current_user_obj.username
	u_name = current_user_obj.username
	profile_obj = Profile.objects.get(user = current_user_obj)
	tree_view_obj = Tree_View.objects.get(user_name=u_name)

	if tree_view_obj.left != "null":
		u_name = tree_view_obj.left
		tree_view_obj = Tree_View.objects.get(user_name=u_name)

		current_user_obj = User.objects.get(username = u_name)
		profile_obj = Profile.objects.get(user = current_user_obj)

		while tree_view_obj.left != "null":
			a = []
			if profile_obj.sponsor_id == name:
				a.append(tree_view_obj)
				a.append(profile_obj)
				l.append(a)
			u_name = tree_view_obj.left
			current_user_obj = User.objects.get(username=u_name)
			profile_obj = Profile.objects.get(user=current_user_obj)
			tree_view_obj = Tree_View.objects.get(user_name=u_name)	

		a =[]
		if profile_obj.sponsor_id == name:
			a.append(tree_view_obj)
			a.append(profile_obj)
			l.append(a)

	else:
		pass

	d = {
		'l' : l,
		'null' : 'null',
	}


	

	return render(request,'profile_templates/myleft_referral.html',d)


def myright_referral(request):
	l = []
	current_user_obj = request.user
	name = current_user_obj.username
	u_name = current_user_obj.username
	profile_obj = Profile.objects.get(user = current_user_obj)
	tree_view_obj = Tree_View.objects.get(user_name=u_name)

	if tree_view_obj.right != "null":
		u_name = tree_view_obj.right
		tree_view_obj = Tree_View.objects.get(user_name=u_name)

		current_user_obj = User.objects.get(username = u_name)
		profile_obj = Profile.objects.get(user = current_user_obj)

		while tree_view_obj.right != "null":
			a = []
			if profile_obj.sponsor_id == name:
				a.append(tree_view_obj)
				a.append(profile_obj)
				l.append(a)
			u_name = tree_view_obj.right
			current_user_obj = User.objects.get(username=u_name)
			profile_obj = Profile.objects.get(user=current_user_obj)
			tree_view_obj = Tree_View.objects.get(user_name=u_name)	

		a =[]
		if profile_obj.sponsor_id == name:
			a.append(tree_view_obj)
			a.append(profile_obj)
			l.append(a)

	else:
		pass

	d = {
		'l' : l,
		'null' : 'null',
	}


	

	return render(request,'profile_templates/myleft_referral.html',d)


	
	return render(request,'profile_templates/myright_referral.html')



def matching_income(request):
	user_obj = request.user
	name = user_obj.username
	print(name)
	objs = All_Matching_Income.objects.filter(user_name=name)

	d={
		'objs':objs,
	}
	return render(request,'profile_templates/matching_income.html',d)


def roi_income(request):
	user_obj = request.user
	name = user_obj.username

	objs = Show_ROI.objects.filter(user_name=name)
	d = {
		'objs' : objs,
	}
	return render(request,'profile_templates/roi_income.html',d)

def direct_income(request):
	user_obj = request.user
	
	objs = DirectSponsor_Income.objects.filter(user=user_obj)
	
	d = {
		'objs' : objs,
	} 
	return render(request,'profile_templates/direct_income.html',d)

				
def withrawl_income(request):
	return render(request,'profile_templates/withrawl_income.html')


def update_kyc(request):
	user_obj = request.user
	obj = Bank_Info.objects.get(user = user_obj)

	
	form = Bank_Form(request.POST or None,instance=obj)
		
	if form.is_valid():
		if obj.cheak==False:
			obj.cheak = True
			form.save()
			obj.save()
	else:
		messages.success(request,f'Contact the Admin!')
	
	d = {
	 'form' : form,
	}
	return render(request,'profile_templates/update_kyc.html',d)

def updating_kyc(request):
	user = request.user
	obj = Bank_Info.objects.get(user=user)
	form = Bank_Form()
	if request.method == 'POST':
		print("snsauhsaiuagi")
		form = Bank_Form(request.POST)
		if form.is_valid():
			print("ojjjj")
	

	d = {
		'form' : form,
	}
	return render(request,'profile_templates/updating_kyc.html',d)




'''
 {% if messages %}
          {% for message in messages%}
           <div class="alert alert-{{message.tag}}">
             {{ message }}
           </div>
          {% endfor %}
        {% endif %}
        
        {% block content %} {% endblock%}
      
'''	