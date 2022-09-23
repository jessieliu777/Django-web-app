from rest_framework import serializers
from project.models import Product, Tag, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    def create(self, data):
        return Category.objects.create(**data)

    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    tagSerializer = TagSerializer(read_only=True)
    categorySerializer = CategorySerializer(read_only=True)

    def create(self, data):
        return Product.objects.create(**data)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id',)
        depth = 2