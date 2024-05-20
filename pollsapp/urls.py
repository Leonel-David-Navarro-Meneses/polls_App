"""
URL configuration for pollsapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path , include
from django.shortcuts import render


def hello(request):
    return HttpResponse('holap como estas')

def multiply(request, num):
    html = f'<h1>tabla del { num }</h1>'
    for i in range(1, 11):
        html += f'<p>{ i } * { num } = { i * num} </p>'
    return HttpResponse(html)

def home(request):
    return render(request,'home.html')

urlpatterns = [
    path('', home , name='home'),
    path('poll/', include('poll.urls')),
    path('admin/', admin.site.urls),
    path('hello/', hello, name='hello'),
    path('table/<int:num>', multiply, name='multiply'),
]
