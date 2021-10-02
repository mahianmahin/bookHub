from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('forget-password', forget_password, name='forget_password'),
    path('reset-password', reset_password, name='reset_password'),
    path('user-dashboard', userDashboard, name='user_dashboard'),
    path('update-profile', updateProfile, name='update_profile'),
]