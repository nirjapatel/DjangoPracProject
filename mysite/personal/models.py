from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save #going to save the default django user object

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=40,default='NYC')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

