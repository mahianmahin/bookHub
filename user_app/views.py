from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


# Create your views here.
def signup(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=email, first_name=f_name, last_name=l_name, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')

def app_login(request):
    print(request.user)
    if request.method == "POST":
        print("1. Initializing Login system")
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("2. User is authenticated")
            print(user)
            login(request, user)
            print("3. User logged in")
            return redirect('/')

        else:
            print("2. User authentication failed")

    return render(request, 'login.html')

def app_logout(request):
    logout(request)
    print("User logged out")

    return redirect('/')

def forget_password(request):
    context = {}
    return render(request, 'forget-password.html', context=context)


def reset_password(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            new_password = request.POST['new_password']
            print(new_password)

            user = User.objects.get(username=request.user)
            user.set_password(new_password)
            user.save()

            print("Password changed")
        
        else:
            return redirect('/login')

    context = {}
    return render(request, 'reset-password.html', context=context)


def userDashboard(request):
    context = {}
    return render(request, 'dashboard.html', context=context)


def updateProfile(request):
    context = {}
    return render(request, 'dashboard.html', context=context)
