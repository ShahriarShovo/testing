from django.dispatch import receiver
from django.db.models.signals import post_save
from user_auth.models.user import User
from user_auth.models.user_profile import Profile


@receiver(post_save,sender=User)
def post_save_create_profile_reciver(sender,instance,created, **kwargs):
    if created:
        attrs_needed= ['first_name', 'last_name']
        Profile.objects.create(user=instance, first_name=instance.first_name,last_name=instance.last_name )

    else:
        try:
            profile=Profile.objects.get(user=instance)
            profile.save()
        except:
            Profile.objects.create(user=instance)



