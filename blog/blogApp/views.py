from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from .models import blog


def home(request):
    return render(request, 'blogApp/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'blogApp/signup.html')
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current')
            else:
                return render(request, 'blogApp/signup.html', {'PassError': "Passwords Didn't Match. Try Again!"})
        except IntegrityError:
            return render(request, 'blogApp/signup.html', {'NameError': "Username Is Already Taken. Try Another One!"})

@login_required(login_url='loginuser')
def current(request):
    blogs = blog.objects.filter(user=request.user)
    return render(request, 'blogApp/current.html', {'blogs': blogs})

@login_required(login_url='loginuser')
def logoutuser(request):
    logout(request)
    return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'blogApp/login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'blogApp/login.html', {
                'error': "Hmmm... Can't Seem To Find This User. If you haven't made an account yet Sign Up, otherwise check if you made any mistakes!"})
        else:
            login(request, user)
            return redirect('current')

@login_required(login_url='loginuser')
def create(request):
    if request.method == "GET":
        return render(request, 'blogApp/create.html', {'form': BlogForm()})
    else:
        try:
            form = BlogForm(request.POST)
            newBlog = form.save(commit=False)
            newBlog.user = request.user
            newBlog.save()
        except ValueError:
            return render(request, 'blogApp/create.html',
                          {'form': BlogForm(), 'error': 'Need a Smaller Title! 100 characters at Most!'})
        return redirect('current')

@login_required(login_url='loginuser')
def detailUp(request, blog_pk):
    Blog = get_object_or_404(blog, pk=blog_pk, user=request.user)
    if request.method == "GET":
        form = BlogForm(instance=Blog)
        return render(request, 'blogApp/detailUp.html', {'blog': Blog, 'form': form})
    else:
        try:
            form = BlogForm(request.POST, instance=Blog)
            form.save()
            return redirect('current')
        except ValueError:
            return render(request, 'blogApp/detailUp.html', {'blog': Blog, 'form': form, 'error': "Bad Data! Try Again!"})


def detail(request, blog_pk):
    Blog = get_object_or_404(blog, pk=blog_pk)
    return render(request, 'blogApp/detail.html', {'blog': Blog})

@login_required(login_url='loginuser')
def delete(request, blog_pk):
    Blog = get_object_or_404(blog, pk=blog_pk, user=request.user)
    if request.method == 'POST':
        Blog.delete()
        return redirect('current')

def search(request):
    term = request.GET.get('search')
    Blog = blog.objects.filter(title__icontains=term)
    return render(request, 'blogApp/search.html', {'blog': Blog, 'term': term})

def aboutMe(request):
    return render(request, 'blogApp/about.html')
