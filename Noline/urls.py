"""Noline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from nolineApp import views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('store/', views.store, name='store'),
    path('review/', views.review, name='review'),
    path('contact/', views.contact, name='contact'),
    
    # include()를 이용하여 url 분할 예정
    path('accounts/login', accounts.views.login, name='login'),
    path('accounts/join', accounts.views.join, name='join'),
    path('accounts/logout', accounts.views.logout, name='logout'),
]
