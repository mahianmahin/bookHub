from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('books/', books, name="books"),
    path('book_details/<int:id>/<str:name>/', book_details, name="book_details"),
    path('blogs/', blogs, name="blogs"),
    path('my_blog/', my_blog, name="my_blog"),
    path('single_blog/<int:id>/<str:title>/', single_blog, name="single_blog"),
    path('delete_blog/<int:id>/', delete_blog, name="delete_blog"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('delete/<int:id>/', delete_book, name="delete"),
    path('search/', search, name="search"),
    path('filter/', filter_books, name="filter"),
    path('subscribe/', subscribe, name="subscribe"),
]
