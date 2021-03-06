"""ziru_app URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from . import views

urlpatterns = [
    path('sleepyfish/', include('app.urls', namespace='app')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]

# 创建assets文件后添加的, 然后到layout.html中添加{% load static %}标签
urlpatterns += staticfiles_urlpatterns()