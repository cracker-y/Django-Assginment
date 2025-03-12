"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import render, redirect
from django.http import Http404
from fake_db import user_db
from todo import views


def user_list(request):
    return render(request, 'user_list.html', {'data': user_db})


def get_user(request, user_id):
    try:
        context = {"data": user_db[user_id], "user_id": user_id}
    except KeyError:
        return Http404()
    return render(request, 'user_info.html', context)


def todo_list(request):
    return render(request, '')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', user_list),
    path('users/<int:user_id>/', get_user),
    path('todo/', views.todo_list),
    path('todo/<int:todo_id>/', views.todo_info),
]
