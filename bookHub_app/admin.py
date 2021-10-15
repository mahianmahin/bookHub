from django.contrib import admin

from .models import *


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name', 'author_name', 'book_rating', 'uploaded_time']

@admin.register(BooksReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'star']

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'source']

@admin.register(BookCategories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']

@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']
