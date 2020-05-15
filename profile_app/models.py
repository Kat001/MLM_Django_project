from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phon_no = models.CharField(max_length=12)
    city = models.CharField(max_length=50)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    package = models.IntegerField(default=1000)
    is_active = models.BooleanField(default=False)
    active_amount = models.IntegerField(default=0)

    def __str__(self):
        return(f'{self.user.username}')


class ROI(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	no = models.CharField(max_length=20)
	date = models.DateField(default='1999-01-01')
	income = models.IntegerField(default=0)

	def __str__(self):
		return(f'{self.user.username}')


class Requested_Fund(models.Model):
	user_name = models.CharField(max_length=20)
	date = models.DateField(default='1999-01-01')
	fund = models.IntegerField(default=0)
	transection_no = models.IntegerField(default=0)
	proof = models.ImageField(default="default.jpg", upload_to="profile_pics")
	status = models.CharField(max_length=10,default="Pending")

	def __str__(self):
		return(f'{self.user_name}')


class Fund(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avail_fund = models.IntegerField(default=0)

	def __str__(self):
		return(f'{self.user.username}')




	
		

