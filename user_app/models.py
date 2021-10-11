from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='users',null=True, blank=True)
    address = models.CharField(max_length=50,null=True, blank=True)
    occupation = models.CharField(max_length=50,null=True, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)
