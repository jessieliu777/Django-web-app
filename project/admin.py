from django.contrib import admin

# Register your models here.
from .models import Tag, Category, Product

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Product)