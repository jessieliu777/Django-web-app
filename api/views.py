from rest_framework.response import Response
from rest_framework.decorators import api_view
from project.models import Product, Category, Tag
from rest_framework import generics, status, mixins
from api.serializers import ProductSerializer, CategorySerializer, TagSerializer

from rest_framework.views import APIView
from django.http import Http404, JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

# Import pagination
from django.core.paginator import Paginator


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'products': reverse('product-list', request=request, format=format)
    })


#
class ProductList(APIView, PageNumberPagination):
    # using APIView
    def get(self, request, format=None):
        page = int(request.query_params.get('page', 0))
        page_size = int(request.query_params.get('page_size', 10))
        products = Product.objects.all().order_by('id')
        if page == 0:
            page_size = products.count()
            page = 1
        paginator = Paginator(products, page_size)
        products_paginated = paginator.page(page)
        serializer = ProductSerializer(products_paginated, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        name = request.data['name']
        category_data = request.data['category']
        category = Category.objects.filter(id=category_data['id'])[0]
        tags = request.data.get('tag', [])

        product = Product.objects.create(name=name, category=category)
        # add tags in the tag table of product
        for tag in tags:
            product.tag.add(tag['id'])
        serializer = ProductSerializer(product)
        try:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryList(APIView):
    # serializer_class = CategorySerializer
    # queryset = Category.objects.all()

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        category = Category.objects.create(name=request.data['name'])
        return Response(request.data, status=status.HTTP_201_CREATED)


class TagList(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class ProductSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TagSingle(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CategorySingle(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
