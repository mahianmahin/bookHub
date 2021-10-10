from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Books(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE())
    name = models.CharField(max_length=30,null=True, blank=True)
    category = models.Choices()
    description = models.CharField(max_length=250,null=True, blank=True)
    upload_time = models.DateTimeField()
    writer_name = models.CharField(max_length=50,null=True, blank=True)

class BooksReview(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE())
    user = models.ForeignKey(User, on_delete=models.CASCADE())
    review = models.CharField(max_length=250, null=True, blank=True)
    star = models.IntegerField()

class Blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE())
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True, blank=True)
    img = models.ImageField()
    created_time = models.DateTimeField()