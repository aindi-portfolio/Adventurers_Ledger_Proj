from django.urls import path
from .views import Sign_Up, Login

urlpatterns = [
    path('/signup', Sign_Up.as_view(), name='signup'),
    path('/login', Login.as_view(), name='login'),
]