from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from profile_app.models import Requested_Fund,Fund
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def admin_page(request):

	return render(request,'admin_templates/index.html')

def send_funds(request):
    rqs = Requested_Fund.objects.all
    print("Data aa gya hai")
    d = {
    	'rqs' : rqs,
    }
    return render(request,'admin_templates/send_funds.html',d)


def update_funds(request,user_name,fund,i_d):

	obj1 = User.objects.get(username=user_name)
	obj = Fund.objects.get(user = obj1 )
	Requested_Fund_obj = Requested_Fund.objects.get(id = i_d)

	obj.avail_fund += fund
	if Requested_Fund_obj.status == "Pending":
		Requested_Fund_obj.status = "Approved"

	obj.save()
	Requested_Fund_obj.save()

	return redirect('send_funds')
	
	

	d= {

	}
	
	return render(request,'admin_templates/update_funds.html',d)

def cancel_funds(request,user_name,fund,i_d):
	Requested_Fund_obj = Requested_Fund.objects.get(id = i_d)
	if Requested_Fund_obj.status == "Pending":
		Requested_Fund_obj.status = "Cancelled"

	Requested_Fund_obj.save()

	return redirect('send_funds')
	return render(request,'admin_templates/cancel_funds.html')
