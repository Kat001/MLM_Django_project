from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phon_no = models.CharField(max_length=12)
    city = models.CharField(max_length=50)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    package = models.IntegerField(default=1000)
    is_active = models.BooleanField(default=False)
    active_amount = models.IntegerField(default=0)
    sponsor_id = models.CharField(max_length=50,default="null")
    side = models.CharField(max_length=5,default = "null")
    #registration_date = models.DateField(default='1999-01-01')
    #activation_date = models.DateField(default='1999-01-01')


    
    @property
    def username(self):
        return self.user.username

    '''class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ("user",)'''



    def __str__(self):
        return(f'{self.user.username}')





class ROI(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	no = models.CharField(max_length=20)
	date = models.DateField(default='1999-01-01')
	income = models.IntegerField(default=0)

	@property
	def username(self):
		return self.user.username

	def __str__(self):
		return(f'{self.user.username}')

class Update_ROI(models.Model):
	income_date = models.DateTimeField(auto_now_add=True,null=True) 
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	activated_amount = models.IntegerField(default=0)
	roi_income = models.IntegerField(default=0)
	starting_date = models.DateTimeField(auto_now_add=True,null=True)
	activated_amount = models.IntegerField(default=0)
	ending_date = models.DateField(default='1920-05-01')
	days = models.IntegerField(default=30)

	@property
	def username(self):
		return self.user.username

	def __str__(self):
		return(f'{self.user.username}')

class Show_ROI(models.Model):
	income_date = models.DateField(auto_now_add=True,null=True)
	user_name = models.CharField(max_length=30,default='')
	roi_income = models.IntegerField(default=0)

	
	def __str__(self):
		return(f'{self.user_name}')



class Requested_Fund(models.Model):
	user_name = models.CharField(max_length=20)
	date = models.DateField(default='1999-01-01')
	fund = models.PositiveIntegerField(default=0)
	transection_no = models.IntegerField(default=0)
	proof = models.ImageField(default="default.jpg", upload_to="profile_pics")
	status = models.CharField(max_length=10,default="Pending")

	def __str__(self):
		return(f'{self.user_name}')


class Fund(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avail_fund = models.PositiveIntegerField(default=0)

	@property
	def username(self):
		return self.user.username



	def __str__(self):
		return(f'{self.user.username}')




class Tree_View(models.Model):
	user_name = models.CharField(max_length=50,unique=True)
	left = models.CharField(max_length=50,default='null')
	right = models.CharField(max_length=50,default='null')
	left_count = models.IntegerField(default=0)
	right_count = models.IntegerField(default=0)


	def __str__(self):
		return(f'{self.user_name}')

class DirectSponsor_Income(models.Model):
	income_date = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	user_name = models.CharField(max_length=30)
	activated_amount  = models.IntegerField(default=0)
	direct_income = models.IntegerField(default=0)

	@property
	def username(self):
		return self.user.username

	def __str__(self):
		return(f'{self.user.username}')



class Matching_Income(models.Model):
	income_date = models.DateTimeField(auto_now_add=True,null=True)
	user_name = models.CharField(max_length=20)
	new_leftBV = models.IntegerField(default=0)
	new_rightBV = models.IntegerField(default=0)
	match_BV = models.CharField(default="0:0",max_length=50)
	matching_income = models.IntegerField(default=0)
	carry_leftBV = models.IntegerField(default=0)
	carry_rightBV = models.IntegerField(default=0)
	total_leftBV = models.IntegerField(default=0)
	total_rightBV = models.IntegerField(default=0)
	collapse_leftBV = models.IntegerField(default=0)
	collapse_rightBV = models.IntegerField(default=0)

	

	def __str__(self):
		return(f'self.username') 

class All_Matching_Income(models.Model):
	income_date = models.DateTimeField(auto_now_add=True,null=True)
	user_name = models.CharField(max_length=20,unique=False)
	new_leftBV = models.IntegerField(default=0)
	new_rightBV = models.IntegerField(default=0)
	match_BV = models.CharField(default="0:0",max_length=50)
	matching_income = models.IntegerField(default=0)
	carry_leftBV = models.IntegerField(default=0)
	carry_rightBV = models.IntegerField(default=0)
	total_leftBV = models.IntegerField(default=0)
	total_rightBV = models.IntegerField(default=0)
	collapse_leftBV = models.IntegerField(default=0)
	collapse_rightBV = models.IntegerField(default=0)

	

	def __str__(self):
		return(f'self.user_name') 



class Binary_Wallet(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	b_income = models.PositiveIntegerField(default=0)
	total_bincome = models.PositiveIntegerField(default=0)

	@property
	def username(self):
		return self.user.username



	def __str__(self):
		return(f'{self.user.username}')


class Roi_Wallet(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	r_income = models.PositiveIntegerField(default=0)
	total_rincome = models.PositiveIntegerField(default=0)

	@property
	def username(self):
		return self.user.username



	def __str__(self):
		return(f'{self.user.username}')


class Direct_Wallet(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	d_income = models.PositiveIntegerField(default=0)
	total_dincome = models.PositiveIntegerField(default=0)

	@property
	def username(self):
		return self.user.username



	def __str__(self):
		return(f'{self.user.username}')


class Bank_Info(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	account_holder_name = models.CharField(max_length=40,default="-")
	account_number = models.CharField(max_length=30,default='-')
	branch_name = models.CharField(max_length=40,default='-')
	ifsc_code = models.CharField(max_length=20,default="-")
	bank_name = models.CharField(max_length=30,default='-')
	nominee_name = models.CharField(max_length=30,default="-")
	aadhar_number = models.CharField(max_length=12,default="-")
	pan_number = models.CharField(max_length=10,default="-")
	aadhar_image = models.ImageField(default="default.jpg", upload_to="profile_pics")
	pan_image = models.ImageField(default="default.jpg", upload_to="profile_pics")
	p_image = models.ImageField(default="default.jpg", upload_to="profile_pics")
	cheak = models.BooleanField(default=False)

	@property
	def username(self):
		return self.user.username



	def __str__(self):
		return(f'{self.user.username}')




'''
b = All_Matching_Income(user_name=name1,new_leftBV=obj.new_leftBV,new_rightBV=obj.new_rightBV,
										match_BV=obj.match_BV,matching_income=obj.matching_income,
										carry_leftBV=obj.carry_leftBV,carry_rightBV=obj.carry_rightBV,
										total_leftBV=obj.total_leftBV,total_rightBV=obj.total_rightBV,
										collapse_leftBV=obj.collapse_leftBV,collapse_rightBV=obj.collapse_rightBV)
				b.save()

'''

	

