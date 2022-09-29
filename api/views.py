from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from project.models import Product, Category, Tag
from rest_framework import generics, status
from api.serializers import ProductSerializer, CategorySerializer, TagSerializer

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

# Import pagination
from django.core.paginator import Paginator
from api.pagination import ProductPagination


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'products': reverse('product-list', request=request, format=format)
    })


#
class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    # queryset = Product.objects.select_related('category').prefetch_related('tag').order_by('id')
    pagination_class = ProductPagination

    def get_queryset(self):
        queryset = Product.objects.select_related('category').prefetch_related('tag').order_by('id')
        name = self.request.query_params.get('name')
        category = self.request.query_params.get('category')
        if name is not None:
            queryset = self.queryset.filter(name=name)
        if category is not None:
            queryset = self.queryset.filter(category__name=name)

        # print(self.pagination_class.page_size);
        return queryset

    # def get(self, request, format=None):
    #     products = self.get_queryset()
    #     page = self.paginate_queryset(products)
    #     serializer = ProductSerializer(page)
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        # name = request.data.get('name', 'unnamed')
        # category_data = request.data.get('category', None)
        # if category_data is None:
        #     return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        # category = Category.objects.filter(id=category_data['id'])[0]
        # tags = request.data.get('tag', [])
        #
        # product = Product.objects.create(name=name, category=category)
        # # add tags in the tag table of product
        # for tag in tags:
        #     product.tag.add(tag['id'])
        # serializer = ProductSerializer(product)
        # try:
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # except:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return self.list(request)


class CategoryList(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    #
    # def get(self, request, format=None):
    #     categories = Category.objects.all()
    #     serializer = CategorySerializer(categories, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     category = Category.objects.create(name=request.data['name'])
    #     return Response(request.data, status=status.HTTP_201_CREATED)


class TagList(ListAPIView):
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
