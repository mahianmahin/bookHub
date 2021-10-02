from django.shortcuts import render


# Create your views here.
def signup(request):
    context = {}
    return render(request, 'signup.html', context=context)


def login(request):
    context = {}
    return render(request, 'login.html', context=context)


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
