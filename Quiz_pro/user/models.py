from django.db import models
from django.contrib.auth.models import User


class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.SmallIntegerField()

def upload_profile_to(instance,filename):
    	return f'profile_picture/{instance.user.username}/{filename}'

	
class Profile(models.Model):
	gen = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	about_me = models.CharField(max_length=250, null=True)
	birthday = models.DateField(null=True)
	profile_pic = models.ImageField(upload_to = upload_profile_to, null=True, default = 'defaults/profile_pic.jpg')
	gender = models.CharField(choices=gen, max_length=6, null=True)
	
	def __str__(self):
		return self.user.username
		
	


