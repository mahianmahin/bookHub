from django.contrib import messages
from django.http import HttpResponse, response
from django.shortcuts import redirect, render
# ========== Custom printing function for debugging ============
from user_app.models import UserProfile

from .models import *


def println(text):
    print("\n====================\n", text, "\n====================\n")


# ========== Custom printing function for debugging ============


# Create your views here.
def home(request):
    context = {
        "home": "active"
    }
    return render(request, 'index.html', context)

def books(request):
    books = Books.objects.all()

    category_dict = {}

    for book in books:
        item = book.book_category
        category = item.split(',')
        
        category_dict[book.id] = category

    println(category_dict)

    context = {
        "books": "active",
        "all_books": books,
        "category": category_dict
    }

    return render(request, 'books.html', context=context)

def book_details(request, id, name):
    book = Books.objects.get(pk=id)
    
    # response = HttpResponse(book.book, content_type='application/pdf')
    # response['Content-Disposition'] = 'filename=%s' % book.book
    
    if request.method == "POST":
        review = request.POST.get('review')
        rating_star = request.POST.get('rating_stars')

        println(review)
        println(rating_star)

        review_ins = BooksReview(
            book = book,
            user = request.user,
            review = review,
            star = rating_star
        )

        review_ins.save()
        messages.info(request, "Review saved")
        

    context = {
        "book": book
    }

    return render(request, 'book-details.html', context=context)

def blogs(request):
    context = {
        "blogs": "active"
    }
    return render(request, 'all-blogs.html', context)

def my_blog(request):
    if request.user.is_authenticated:
        context = {
            "my_blog": "active"
        }
        return render(request, 'blog.html', context)
    
    else:
        messages.warning(request, "You must be logged in")
        return redirect('/login')

def single_blog(request):
    return render(request, 'single-blog.html')

def contact(request):
    context = {
        "contact": "active"
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        "about": "active"
    }
    return render(request, 'about-us.html', context)

