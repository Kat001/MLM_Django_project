from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from profile_app.models import Profile,ROI,Fund,Tree_View
from profile_app.models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created,**kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()

@receiver(post_save, sender=User)
def create_ROI(sender, instance, created,**kwargs):
	if created:
		ROI.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_ROI(sender, instance, **kwargs):
	instance.roi.save()


@receiver(post_save, sender=User)
def create_fund(sender, instance, created,**kwargs):
	if created:
		Fund.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_fund(sender, instance, **kwargs):
	instance.fund.save()

@receiver(post_save, sender=User)
def create_binary_wallet(sender, instance, created,**kwargs):
	if created:
		Binary_Wallet.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_binary_wallet(sender, instance, **kwargs):
	instance.binary_wallet.save()


@receiver(post_save, sender=User)
def create_roi_wallet(sender, instance, created,**kwargs):
	if created:
		Roi_Wallet.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_roi_wallet(sender, instance, **kwargs):
	instance.roi_wallet.save()

@receiver(post_save, sender=User)
def create_direct_wallet(sender, instance, created,**kwargs):
	if created:
		Direct_Wallet.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_direct_wallet(sender, instance, **kwargs):
	instance.direct_wallet.save()



