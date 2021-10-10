from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('books/', books, name="books"),
    path('blogs/', blogs, name="blogs"),
    path('my_blog/', my_blog, name="my_blog"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
]
