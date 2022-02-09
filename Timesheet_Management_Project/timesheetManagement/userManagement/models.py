from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(models.Model): # naming your model User as well, there will be conflict between auth_user and userManagenet_user, since django has some built in functionality to implement authentication. This may create problem in few activitities. I suggest name it different
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    image=models.ImageField(upload_to='userManagement/',null=True, blank=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            User.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user.save()

