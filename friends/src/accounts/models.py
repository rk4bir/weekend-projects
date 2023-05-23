from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from main.utils import get_random_number
from django.shortcuts import reverse
from django.db.models import Q



class Account(models.Model):
    user 			= models.OneToOneField(User, on_delete=models.CASCADE)
    photo 			= models.ImageField(
        upload_to="profile_photos/",
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field",
    )
    drive_photo_link= models.CharField(max_length=1000, default='', blank=True, null=True)
    height_field    = models.IntegerField(default=0)
    width_field     = models.IntegerField(default=0)

    is_active       = models.BooleanField(default=True)

    activation_code = models.CharField(max_length=10, blank=True, null=True)
    activation_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    forgotpass_code = models.CharField(max_length=10, blank=True, null=True)

    recover_code    = models.CharField(max_length=10, blank=True, null=True)
    recover_time    = models.DateTimeField(blank=True, null=True)

    about_me	    = models.TextField(default='', blank=True)






    def __str__(self):
        return self.user.email + ' - ' + self.user.get_full_name()


    def get_profile_link(self):
        return reverse('accounts:index')

    def get_public_profile_link(self):
        return reverse('accounts:public-profile', kwargs={'username': self.user.username})


def pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.activation_code:
		instance.activation_code = get_random_number(size=6)
	if not instance.forgotpass_code:
		instance.forgotpass_code = get_random_number(size=4)
	if not instance.recover_code:
		instance.recover_code = get_random_number(size=6)

pre_save.connect(pre_save_receiver, sender=Account)