"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogApp import views

urlpatterns = [
    #Admin Stuff
    path('admin/', admin.site.urls),

    #Web Pages
    path('', views.home, name='home'),
    path('current/', views.current, name='current'),
    path('search/', views.search, name='search'),
    path('about/', views.aboutMe, name="aboutMe"),

    #Authentication
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    #CRUD
    path('create/', views.create, name='create'),
    path('blog/<int:blog_pk>', views.detail, name='detail'),
    path('blog/<int:blog_pk>/update', views.detailUp, name='detailUp'),
    path('blog/<int:blog_pk>/delete', views.delete, name='delete'),

]
