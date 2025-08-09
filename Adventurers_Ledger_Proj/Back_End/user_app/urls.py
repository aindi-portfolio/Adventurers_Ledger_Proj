from django.urls import path
from .views import Sign_Up, Login, Logout, User_Profile

urlpatterns = [
    path('signup', Sign_Up.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('profile', User_Profile.as_view(), name='profile'),
]