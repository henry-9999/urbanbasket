from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import Blog
from datetime import datetime
# Create your views here.




def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email alerady exists")
                return redirect('signup')
            else:
                user = User.objects.create_user(email=email,username=username,first_name=firstname,last_name=lastname,password=password)
                user.save()
                messages.info(request,"Account createdSuccesfully")
                return redirect('login')
        else:
            messages.info(request,"password are not the same")
            return redirect("signup")
                
    return render(request,'signup.html')


def product(request):
    return render(request,'product.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credencials')
            return redirect('login')
    return render(request,'login.html')


def contactus(request):
    return render(request,'contactus.html')


def blog(request):
    blogs = Blog.objects.all()
    return render(request,'blog.html',{'blogs':blogs})


def aboutus(request):
    return render(request,'about.html')
def profile(request):
    return render(request,'profile.html')


def single_blog(request,pk):
    blog = Blog.objects.get(id=pk)
    return render(request,'singleblog.html',{"blog":blog})



def add_blog(request):
    if request.method == "POST":
        if User.is_authenticated:
            image_url = request.POST['image_url']
            header = request.POST['title']
            text = request.POST['text']
            Blog.objects.create(image=image_url,header=header,text=text)
            return redirect('blog')
    return render(request,'addBlog.html')



