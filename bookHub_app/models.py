from datetime import datetime

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class Books(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.FileField(upload_to='pdf')
    book_thumbnail = models.ImageField(upload_to='pdf/thumbnails', null=True)
    book_name = models.CharField(max_length=200, null=True)
    language = models.CharField(max_length=100, null=True)
    author_name = models.CharField(max_length=200, null=True)
    description = models.TextField()
    uploaded_time = models.DateTimeField(auto_now=True)
    book_category = models.CharField(max_length=1000, null=True)
    book_rating = models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return self.book_name + '.pdf'


class BooksReview(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=250, null=True, blank=True)
    star = models.IntegerField(default=0, null=True)

class Blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='blog_img')
    created_time = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return self.title

class Quote(models.Model):
    quote = models.TextField(max_length=115)
    source = models.CharField(max_length=20)

class BookCategories(models.Model):
    category = models.CharField(max_length=20)

class Subscribers(models.Model):
    email = models.EmailField(max_length=300)


# Signal for new book upload
@receiver(post_save, sender=Books)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        subscribers_list = []
        subs = Subscribers.objects.all()

        for subscribers in subs:
            subscribers_list.append(subscribers.email)

        print(subscribers_list)

        html_content = render_to_string('emails/new_book_email.html')
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            "A new book has just been uploaded",
            text_content,
            "BookHub Team",
            subscribers_list
        )

        email.attach_alternative(html_content, "text/html")
        email.send()
        
# Signal for new blog upload
@receiver(post_save, sender=Blogs)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        subscribers_list = []
        subs = Subscribers.objects.all()

        for subscribers in subs:
            subscribers_list.append(subscribers.email)

        print(subscribers_list)

        html_content = render_to_string('emails/new_blog_email.html')
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            "A new blog has just been uploaded",
            text_content,
            "BookHub Team",
            subscribers_list
        )

        email.attach_alternative(html_content, "text/html")
        email.send()
        

