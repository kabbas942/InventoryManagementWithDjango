from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.models import User
from Account.models import Profile
from django.dispatch import receiver
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(UserId=instance)
    else:
        try:
            instance.profile.save()
        except Profile.DoesNotExist:
            # If the profile doesn't exist, create it
            Profile.objects.create(UserId=instance) 

@receiver(user_logged_out)
def create_profile_if_missing(sender, user, request, **kwargs):
    try:
        profile = Profile.objects.get(UserId=user)
        print(profile)
    except Profile.DoesNotExist:
        # If the profile doesn't exist, create one
        Profile.objects.create(UserId=user)