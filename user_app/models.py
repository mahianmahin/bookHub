from bookHub_app.models import *
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='users',default='user.jpg')
    address = models.CharField(max_length=50,null=True, blank=True)
    occupation = models.CharField(max_length=50,null=True, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)

