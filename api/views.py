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
        page = int(request.GET.get('page', 1))
        print(request.GET)
        page_size = 100
        products = Product.objects.all().order_by('id')
        paginator = Paginator(products, page_size)
        products_paginated = paginator.page(page)
        serializer = ProductSerializer(products_paginated, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        name = request.data['name']
        category_data = request.data['category']
        category = Category.objects.filter(id=category_data['id'])[0]
        tags = request.data.get('tag', [])

        product = Product.objects.create(name=name, category=category)
        # add tags in the tag table of product
        for tag in tags:
            product.tag.add(tag['id'])

        return Response(request.data, status=status.HTTP_201_CREATED)
        # serializer = ProductSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryList(APIView):
    # serializer_class = CategorySerializer
    # queryset = Category.objects.all()

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # serializer = CategorySerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        category = Category.objects.create(name=request.data['name'])
        return Response(request.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagList(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class ProductSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # using mixins
    # def get_object(self, pk):
    #     try:
    #         return Product.objects.get(pk=pk)
    #     except Product.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # using APIView
    # def get(self, request, pk, format=None):
    #     product = self.get_object(pk)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)


class TagSingle(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CategorySingle(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
