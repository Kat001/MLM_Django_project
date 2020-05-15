from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from profile_app.models import Profile,ROI,Fund


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




