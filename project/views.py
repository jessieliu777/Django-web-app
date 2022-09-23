from django.shortcuts import render
from django.views.generic import View

from django.db.models import Q
from project.models import Product
from rest_framework import generics
from api.serializers import ProductSerializer


# Create your views here.

class RenderViewFrontend(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


def index(request):
    return render(request, 'index.html')


def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(Q(name__contains=searched) | Q(category__name__contains=searched) | Q(
            tag__name__contains=searched)).distinct()
        return render(request, 'search_results.html', {'searched': searched, 'products': products})
    else:
        return render(request, 'search_results.html')


def filter_results(request):
    if request.method == "POST":
        name = request.POST['name']
        category = request.POST['category']
        tag = request.POST['tag']
        products = Product.objects.filter(
            Q(name__contains=name) & Q(category__name__contains=category) & Q(tag__name__contains=tag)).distinct()
        return render(request, 'project/filter_results.html', {'products': products})
    else:
        return render(request, 'project/filter_results.html')
