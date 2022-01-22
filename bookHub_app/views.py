from django.contrib import messages
from django.contrib.admin.decorators import register
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import FileResponse, HttpResponse, response
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from user_app.models import UserProfile
import os
from django.conf import settings
from .models import *

# ========== Custom printing function for debugging ============

def println(text):
    print("\n====================\n", text, "\n====================\n")

# ========== Custom printing function for debugging ============


# Create your views here.
def home(request):
    site_utils = SiteUtils.objects.all()
    reviews = BooksReview.objects.all()
    quotes = Quote.objects.all()

    books = Books.objects.all()
    blogs = Blogs.objects.all()
    users = UserProfile.objects.all()

    context = {
        "home": "active",
        "reviews": reviews,
        "quotes": quotes,
        "utils": site_utils,

        "books_len": len(books),
        "blogs_len": len(blogs),
        "users_len": len(users),
        "reviews_len": len(reviews)
    }
    return render(request, 'index.html', context)


def books(request):
    books = Books.objects.all()
    book_categories = BookCategories.objects.all()

    category_dict = {}

    for book in books:
        item = book.book_category
        category = item.split(',')

        category_dict[book.id] = category

    println(category_dict)

    context = {
        "books": "active",
        "all_books": books,
        "category": category_dict,
        "book_categories": book_categories
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

    messages.info(request, "Book deleted")

    return redirect('/user-dashboard')


def book_details(request, id, name):
    book = Books.objects.get(pk=id)
    reviews = BooksReview.objects.filter(book=book)
    if request.method == "GET":

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

        from django.core.files.storage import FileSystemStorage
        from django.http import HttpResponse, HttpResponseNotFound
        from django.templatetags.static import static

        fs = FileSystemStorage()
        filename = book.book.url
        print(filename)

        # return render(request, 'book-details.html', {'book': book})
        # path = open(filename, 'rb')
        # with open(path, 'rb') as pdf:
        #     print(pdf)
        # print(type(path))
        # if fs.exists(filename):
        #     println("Exists")
        #     with fs.open(filename) as pdf:
        #         response = HttpResponse(pdf, content_type='application/pdf')
        #         #response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"' #user will be prompted with the browser’s open/save file
        #         response['Content-Disposition'] = 'inline; filename="mypdf.pdf"' #user will be prompted display the PDF in the browser

                # return response

        # else:
        #     return HttpResponseNotFound('The requested pdf was not found in our server.')

        println(response)


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

            messages.info(request, "Blog uploaded")

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

def delete_blog(request, id):
    blog_ins = Blogs.objects.get(id=id)
    blog_ins.delete()
    messages.info(request, "Book deleted")
    return redirect('/my_blog')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        msg = name + "\n" + email + "\n" + subject + "\n\n" + message

        send_mail(
            "Someone wants to contact BookHub",
            msg,
            "BookHub Team",
            ['mahianmahin@yahoo.com', 'shuvro.aps.75@gmail.com'],
            fail_silently=False
        )

        recepient = name

        html_content = render_to_string('emails/contact_email.html', { 
                "recepient": recepient
            })
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            "Contact Response",
            text_content,
            "BookHub Team",
            [email]
        )

        email.attach_alternative(html_content, "text/html")
        email.send()

    context = {
        "contact": "active"
    }
    return render(request, 'contact.html', context)


def about(request):
    site_utils = SiteUtils.objects.all()

    context = {
        "about": "active",
        "utils": site_utils
    }
    return render(request, 'about-us.html', context)

def search(request):
    if request.method == "POST":
        if 'searched' in request.POST:
            searched = request.POST.get('searched')

            books = Books.objects.filter(book_name__contains=searched) | Books.objects.filter(author_name__contains=searched)

            book_categories = BookCategories.objects.all()

            category_dict = {}

            for book in books:
                item = book.book_category
                category = item.split(',')

                category_dict[book.id] = category
            
    context = {
        "searched": searched,
        "all_books": books,
        "category": category_dict,
    }
    return render(request, 'search.html', context=context)

def filter_books(request):

    if request.method == "POST":
        searched_category = request.POST.get('category')

        books = Books.objects.filter(book_category__contains=searched_category)
        book_categories = BookCategories.objects.all()

        category_dict = {}

        for book in books:
            item = book.book_category
            category = item.split(',')

            category_dict[book.id] = category

    context = {
        'searched_category': searched_category,
        "category": category_dict,
        'book_categories': book_categories,
        'all_books': books
    }
    return render(request, 'filter.html', context=context)

def subscribe(request):
    subscribers = Subscribers.objects.all()

    if request.method == "POST":
        subs_email = request.POST.get('subs_email')
        subscribers = Subscribers.objects.all()

        subscribers_list = []
        
        for email in subscribers:
            subscribers_list.append(email.email)

        if subs_email in subscribers_list:
            messages.warning(request, "You are already subscribed")
        else:
            subscribers_ins = Subscribers(email=subs_email)
            subscribers_ins.save()
            messages.info(request, "Subscribed")

            # send welcome email here
            if request.user.is_authenticated:
                recepient = str(request.user.first_name) + " " + str(request.user.last_name)
            else:
                recepient = subs_email

            html_content = render_to_string('emails/subscribe_email.html', { 
                    "recepient": recepient
                })
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                "Thanks for subscribing",
                text_content,
                "BookHub Team",
                [subs_email]
            )

            email.attach_alternative(html_content, "text/html")
            email.send()


    return redirect('/')

