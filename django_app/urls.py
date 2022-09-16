"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from api import views

from project.views import index
from project.views import search_results
from project.views import products_all
from project.views import filter_results

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/', include('api.urls')),
    path('add/', views.addData),
    path('search/', search_results, name='search_results'),
    path('products/', products_all, name='products_all'),
    path('filter/', filter_results, name='filter_results')
]
