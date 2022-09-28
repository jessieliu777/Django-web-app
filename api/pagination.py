from rest_framework.pagination import PageNumberPagination

from project.models import Product


class ProductPagination(PageNumberPagination):
    page_size = 10
    # page_size_query_param = 'page_size'