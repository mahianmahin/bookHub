from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', app_login, name='login'),
    path('logout', app_logout, name='logout'),
    path('forget-password', forget_password, name='forget_password'),
    path('reset-password', reset_password, name='reset_password'),
    path('user-dashboard', userDashboard, name='user_dashboard'),
    path('code-auth', code_authentication, name="code"),
    path('reset-forgetten-password', reset_forget_pass, name="reset_forgetten_pass"),
]
