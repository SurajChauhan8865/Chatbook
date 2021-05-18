"""Chetbook URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from .settings import *
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home,name='Home'),
    path('signup/', views.SignUp,name='SignUp'),
    path('forget/', views.ForgetPassword,name='ForgetPassword'),
    path('profile/', views.Profile,name='Profile'),
    path('profile2/', views.Profile2,name='Profile2'),
    path('logout/', views.Logout,name='Logout'),
    path('editprofile/', views.EditProfile,name='EditProfile'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=MEDIA_ROOT)