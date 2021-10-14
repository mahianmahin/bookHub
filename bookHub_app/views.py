from django.contrib import messages
from django.http import HttpResponse, response
from django.shortcuts import redirect, render
from user_app.models import UserProfile

from .models import *

# ========== Custom printing function for debugging ============

def println(text):
    print("\n====================\n", text, "\n====================\n")

# ========== Custom printing function for debugging ============


# Create your views here.
def home(request):
    reviews = BooksReview.objects.all()
    quotes = Quote.objects.all()

    books = Books.objects.all()
    blogs = Blogs.objects.all()
    users = UserProfile.objects.all()

    context = {
        "home": "active",
        "reviews": reviews,
        "quotes": quotes,

        "books_len": len(books),
        "blogs_len": len(blogs),
        "users_len": len(users),
        "reviews_len": len(reviews)
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


def rating_updater(id, book, rating):
    if rating == 0:
        book.book_rating = 0.0
    else:
        book.book_rating = rating
    book.save()

    return rating


def delete_book(request, id):
    book_ins = Books.objects.get(pk=id)
    book_ins.delete()

    return redirect('/user-dashboard')


def book_details(request, id, name):
    book = Books.objects.get(pk=id)
    reviews = BooksReview.objects.filter(book=book)

    try:
        rating_raw = 0

        for rating in reviews:
            rating_raw += rating.star

        rating = rating_raw / len(reviews)
        rating = round(rating, 1)

        avg_rating = rating_updater(id, book, rating)
    except:
        avg_rating = 0
        rating = 0

    # response = HttpResponse(book.book, content_type='application/pdf')
    # response['Content-Disposition'] = 'filename=%s' % book.book

    if request.method == "POST":
        review = request.POST.get('review')
        rating_star = request.POST.get('rating_stars')

        println(review)
        println(rating_star)

        review_ins = BooksReview(
            book=book,
            user=request.user,
            review=review,
            star=rating_star,
        )

        review_ins.save()
        messages.info(request, "Review saved")
        return redirect('/book_details/' + str(id) + '/' + name + '/')

    context = {
        "book": book,
        "reviews": reviews,
        "rating": rating,
        "review_count": len(reviews)
    }

    return render(request, 'book-details.html', context=context)


def blogs(request):
    blogs_ins = Blogs.objects.all()
    context = {
        "blogs": "active",
        "blogs_ins": blogs_ins
    }
    return render(request, 'all-blogs.html', context)


def my_blog(request):
    if request.user.is_authenticated:
        my_blog_ins = Blogs.objects.filter(user_id=request.user.id).exists()
        if my_blog_ins:
            my_blogs = Blogs.objects.filter(user_id=request.user.id)
        else:
            my_blogs = {}
        if request.method == "POST":
            title = request.POST.get('title')
            description = request.POST.get('description')
            thumbnail = request.FILES['img']
            blog_ins = Blogs(user_id=request.user.id, title=title, description=description, thumbnail=thumbnail)
            blog_ins.save()

            context = {
                "my_blog": "active",
            }
            return redirect('my_blog')

        context = {
            "my_blog": "active",
            "my_blogs": my_blogs
        }
        return render(request, 'blog.html', context)

    else:
        messages.warning(request, "You must be logged in")
        return redirect('/login')


def single_blog(request,id, title):
    blog_ins = Blogs.objects.get(id=id)
    blog_author = blog_ins.user_id

    author_blogs = Blogs.objects.filter(user_id=blog_author)
    print("blog_author: ", blog_author)
    context = {
        "blog_ins": blog_ins,
        "author_blogs": author_blogs
    }
    return render(request, 'single-blog.html', context)


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

def search(request):
    if request.method == "POST":
        if 'searched' in request.POST:
            searched = request.POST.get('searched')

            books = Books.objects.filter(book_name__contains=searched) | Books.objects.filter(author_name__contains=searched)
            
    context = {
        "searched": searched,
        "all_books": books
    }
    return render(request, 'search.html', context=context)
