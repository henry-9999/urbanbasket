from django.urls import path
from . import views
from main.views import *



urlpatterns = [
    path('',home,name="home"),
    path('signup',signup,name="signup"),
    path('product',product,name="product"),
    path('logout',logout,name="logout"),
    path('login',login,name="login"),
    path('contactus',contactus,name="contactus"),
    path('blog',blog,name="blog"),
    path('aboutus',aboutus,name="aboutus"),
    path('profile',profile,name="profile"),
    path('blog/<str:pk>',single_blog,name="single post"),
    path('addblog',add_blog,name="Add post")
    
]