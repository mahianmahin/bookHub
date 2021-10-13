from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('books/', books, name="books"),
    path('book_details/<int:id>/<str:name>/', book_details, name="book_details"),
    path('blogs/', blogs, name="blogs"),
    path('my_blog/', my_blog, name="my_blog"),
    path('single_blog/', single_blog, name="single_blog"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about")
]
