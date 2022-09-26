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

from django.urls import path
from api.views import ProductList, ProductSingle, CategoryList, CategorySingle, TagList, TagSingle, api_root
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path(r'products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>', ProductSingle.as_view(), name='product-single'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', CategorySingle.as_view(), name='category-single'),
    path('tags/', TagList.as_view(), name='tag-list'),
    path('tags/<int:pk>', TagSingle.as_view(), name='tag-single'),
    path('', api_root)
])
