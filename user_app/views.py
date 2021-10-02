from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(username=email, first_name=f_name, last_name=l_name, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(username,password,  user)

            if user is not None:
                print("laksdfjl")
                login(request, user)
                return redirect('home')
            else:
                print("else")
                messages.info(request, 'Username or Password incorrect')
                return render(request, "login.html", )

    return render(request, 'login.html')


def forget_password(request):
    context = {}
    return render(request, 'forget-password.html', context=context)


def reset_password(request):
    context = {}
    return render(request, 'reset-password.html', context=context)


def userDashboard(request):
    context = {}
    return render(request, 'dashboard.html', context=context)


def updateProfile(request):
    context = {}
    return render(request, 'dashboard.html', context=context)
