from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import User
from .models import *

# Register your models here.

class RequestFund_Admin(admin.ModelAdmin):
	list_display = ('user_name','date','fund','transection_no','proof','status')
	search_fields = ('user_name',)
	readonly_fields = ('user_name','date')
    #filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	actions = ['send_funds','cancel_funds']

	def send_funds(self, request, queryset):
		for obj in queryset:
			if obj.status=='Pending':
				name = obj.user_name
				r_fund = obj.fund
				user_obj = User.objects.get(username=name)
				fund_obj = Fund.objects.get(user=user_obj)
				fund_obj.avail_fund += r_fund
				obj.status = 'Approved'
				fund_obj.save()
				obj.save()

	def cancel_funds(self,request,queryset):
		queryset.update(status="Cancelled")


class Profile_Admin(admin.ModelAdmin):
	list_display = ('username','sponsor_id','side','active_amount','phon_no','city','image','is_active',)
	search_fields = ['user__username']
	#readonly_fields = ('sponsor_id','username','side')
	#filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class ROI_Admin(admin.ModelAdmin):
	list_display = ('username','date','income')
	search_fields = ['user__username']
	readonly_fields = ('username',)
	#filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	

class UpdateROI_Admin(admin.ModelAdmin):
	list_display = ('income_date','username',
					'activated_amount','roi_income','starting_date',
					'ending_date')
	search_fields = ['user__username']
	readonly_fields = ('username',)
	#filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	actions = ['update_roi_income']

	def update_roi_income(self,request,queryset):
		for obj in queryset:
			income = (obj.activated_amount * 5)/100
			obj.roi_income = income
			obj.save()

		objs = ROI.objects.all()

		for obj in objs:
			income = 0
			ob = Update_ROI.objects.filter(user = obj.user)
			for o in ob:
				income += o.roi_income 
			#print(income)
			obj.income = income
			obj.save()

			R = Show_ROI(user_name=obj.user.username,roi_income=income)
			R.save()


		objv = Roi_Wallet.objects.all()
		for obj in objv:
			ob = ROI.objects.get(user = obj.user)
			obj.r_income += ob.income
			obj.total_rincome += ob.income
			obj.save()

		

class ShowROI_Admin(admin.ModelAdmin):
	list_display = ('income_date','user_name','roi_income')
	search_fields = ['user_name','income_date']
	#readonly_fields = ('user_name','income_date')
	#filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class DirectSponsorIncome_Admin(admin.ModelAdmin):
	list_display = ('income_date','username','user_name','activated_amount','direct_income')
	search_fields = ['username','income_date']
	#readonly_fields = ('user_name','income_date')
	#filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


class Fund_Admin(admin.ModelAdmin):
	list_display = ('username','avail_fund')
	search_fields = ['user__username']
	readonly_fields = ('username',)
	#filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class TreeView_Admin(admin.ModelAdmin):
	list_display = ('user_name','left','right','left_count','right_count')
	search_fields = ['user_name']
	#readonly_fields = ('user_name',)
	list_filter = ()
	fieldsets = ()

class MatchingIncome_Admin(admin.ModelAdmin):
	list_display = ('income_date','user_name','new_leftBV','new_rightBV',
					'match_BV','matching_income','carry_leftBV','carry_rightBV',
					'total_leftBV','total_rightBV','collapse_leftBV','collapse_rightBV')
	search_fields=['income_date','user_name']
	readonly_fields=('income_date',)
	list_filter = ()
	fieldsets = ()
	actions = ['Send_Matching_Income']

	def Send_Matching_Income(self, request, queryset):
		for obj in queryset:
			name1 = obj.user_name
			perfect_obj = User.objects.get(username=name1)
			perfect_profile_obj = Profile.objects.get(user = perfect_obj)
			#print(perfect_profile_obj.is_active)

			#income_date = obj.income_date
			'''c_new_leftBV = obj.new_leftBV
			c_new_rightBV = obj.new_rightBV
			c_match_BV = obj.match_BV
			c_matching_income = obj.matching_income
			c_carry_leftBV = obj.carry_leftBV
			c_carry_rightBV = obj.carry_rightBV
			c_total_leftBV = obj.total_leftBV
			c_total_rightBV = obj.total_rightBV'''
			leftBV = 0
			

			current_user_obj = User.objects.get(username = name1)
			profile_obj = Profile.objects.get(user=current_user_obj)
			tree_view_obj = Tree_View.objects.get(user_name=name1)

			if tree_view_obj.left != "null":
				u_name = tree_view_obj.left
				tree_view_obj = Tree_View.objects.get(user_name=u_name)

				current_user_obj = User.objects.get(username = u_name)
				profile_obj = Profile.objects.get(user = current_user_obj)

				stack = [tree_view_obj]
				leftBV += profile_obj.active_amount
				
				
				while len(stack)>0:
					item = stack.pop()
					
					
					if item.left != "null":
						name = item.left
						item1 = Tree_View.objects.get(user_name=name)

						current_user_obj = User.objects.get(username=name)
						profile_obj = Profile.objects.get(user=current_user_obj)
						leftBV += profile_obj.active_amount
						stack.append(item1)

					if item.right != "null":
						name = item.right
						item2 = Tree_View.objects.get(user_name=name)

						current_user_obj = User.objects.get(username=name)
						profile_obj = Profile.objects.get(user=current_user_obj)
						leftBV += profile_obj.active_amount
						stack.append(item2)
			
			rightBV = 0
			current_user_obj = User.objects.get(username = name1)
			profile_obj = Profile.objects.get(user=current_user_obj)
			tree_view_obj = Tree_View.objects.get(user_name=name1)
			if tree_view_obj.right != "null":
				u_name = tree_view_obj.right
				tree_view_obj = Tree_View.objects.get(user_name=u_name)

				current_user_obj = User.objects.get(username = u_name)
				profile_obj = Profile.objects.get(user = current_user_obj)

				stack = [tree_view_obj]
				rightBV += profile_obj.active_amount
				
				
				while len(stack)>0:
					item = stack.pop()
					
					
					if item.left != "null":
						name = item.left
						item1 = Tree_View.objects.get(user_name=name)

						current_user_obj = User.objects.get(username=name)
						profile_obj = Profile.objects.get(user=current_user_obj)
						rightBV += profile_obj.active_amount
						stack.append(item1)

					if item.right != "null":
						name = item.right
						item2 = Tree_View.objects.get(user_name=name)

						current_user_obj = User.objects.get(username=name)
						profile_obj = Profile.objects.get(user=current_user_obj)
						rightBV += profile_obj.active_amount
						stack.append(item2)





			
			obj.new_leftBV = leftBV - obj.total_leftBV
			obj.total_leftBV = leftBV


			obj.new_rightBV = rightBV - obj.total_rightBV
			obj.total_rightBV = rightBV
			

			obj.carry_leftBV += obj.new_leftBV
			obj.carry_rightBV += obj.new_rightBV
			obj.save()

			if obj.carry_leftBV>=obj.carry_rightBV:
				if obj.carry_rightBV>200000:
					income = (200000 * 15)/100
					obj.collapse_rightBV = obj.carry_rightBV-200000
					obj.collapse_leftBV = obj.collapse_rightBV-200000
				else:
					income = (obj.carry_rightBV * 15)/100
					obj.collapse_rightBV = 0
					obj.collapse_leftBV= 0

				obj.matching_income = income
				obj.match_BV = str(income)+" : "+str(income)
				obj.carry_leftBV -= obj.carry_rightBV 
				obj.carry_rightBV = 0
		
			else:
				if obj.carry_leftBV>200000:
					income = (200000 * 15)/100
					obj.collapse_leftBV = obj.carry_leftBV-200000
					obj.collapse_rightBV = obj.carry_leftBV-200000
				else:
					income = (obj.carry_leftBV * 15)/100
					obj.collapse_rightBV = 0
					obj.collapse_leftBV= 0

				obj.matching_income = income
				obj.match_BV = str(income)+" : "+str(income)
				obj.carry_rightBV -= obj.carry_leftBV
				obj.carry_leftBV = 0

			if perfect_profile_obj.is_active == False:
				obj.matching_income = 0

			b = All_Matching_Income(user_name=name1,new_leftBV=obj.new_leftBV,new_rightBV=obj.new_rightBV,
										match_BV=obj.match_BV,matching_income=obj.matching_income,
										carry_leftBV=obj.carry_leftBV,carry_rightBV=obj.carry_rightBV,
										total_leftBV=obj.total_leftBV,total_rightBV=obj.total_rightBV,
										collapse_leftBV=obj.collapse_leftBV,collapse_rightBV=obj.collapse_rightBV)
			b.save()

			current_user_obj = User.objects.get(username = name1)

			BW = Binary_Wallet.objects.get(user = current_user_obj)
			BW.b_income += income
			BW.total_bincome += income
			BW.save()

			obj.save()
				
class AllMatchingIncome_Admin(admin.ModelAdmin):
	list_display = ('income_date','user_name','new_leftBV','new_rightBV',
					'match_BV','matching_income','carry_leftBV','carry_rightBV',
					'total_leftBV','total_rightBV','collapse_leftBV','collapse_rightBV')
	search_fields=['income_date','user_name']
	#readonly_fields=('income_date',)
	list_filter = ()
	fieldsets = ()
	

class BinaryWallet_Admin(admin.ModelAdmin):
	list_display = ('username','b_income','total_bincome',)
	search_fields = ['username']
	#readonly_fields = ('user_name','income_date')
	#filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class RoiWallet_Admin(admin.ModelAdmin):
	list_display = ('username','r_income','total_rincome',)
	search_fields = ['username']
	#readonly_fields = ('user_name','income_date')
	#filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


class DirectWallet_Admin(admin.ModelAdmin):
	list_display = ('username','d_income','total_dincome',)
	search_fields = ['username']
	#readonly_fields = ('user_name','income_date')
	#filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class BankInfo_Admin(admin.ModelAdmin):
	list_display = ('username','bank_name','account_holder_name','account_number','ifsc_code',
					'aadhar_number','pan_number')
	search_fields = ['username']









admin.site.register(Profile,Profile_Admin)

admin.site.register(Matching_Income,MatchingIncome_Admin)
admin.site.register(All_Matching_Income,AllMatchingIncome_Admin)

admin.site.register(Requested_Fund,RequestFund_Admin)
admin.site.register(Fund,Fund_Admin)

admin.site.register(ROI,ROI_Admin)
admin.site.register(Update_ROI,UpdateROI_Admin)
admin.site.register(Show_ROI,ShowROI_Admin)

admin.site.register(DirectSponsor_Income,DirectSponsorIncome_Admin)

admin.site.register(Binary_Wallet,BinaryWallet_Admin)
admin.site.register(Roi_Wallet,RoiWallet_Admin)
admin.site.register(Direct_Wallet,DirectWallet_Admin)

admin.site.register(Tree_View,TreeView_Admin)
admin.site.register(Bank_Info,BankInfo_Admin)

