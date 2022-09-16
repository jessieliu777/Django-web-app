from rest_framework.response import Response
from rest_framework.decorators import api_view
from project.models import Product, Tag
from rest_framework import generics
from api.serializers import ProductSerializer, TagSerializer

@api_view(['GET'])
def getData(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view([''])
def addData(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        tag = self.request.query_params.get('Tag')
        if tag is not None:
            queryset = queryset.filter(tag=tag)
        return queryset

class TagList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductSingle(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class TagSingle(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()