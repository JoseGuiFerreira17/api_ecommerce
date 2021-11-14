from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import parsers
from rest_framework.decorators import permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from product.models import Category, Product
from product.permissions import IsAdminOrReadOnly
from product.serializers import (
    CategorySerializer, ProductSerializer
)


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = (
        'name', 'parent', 'parent__slug', 'parent__name', 'slug'
    )
    search_fields = [
        'name', 'parent__slug', 'parent__name', 'slug'
        ]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    ordering = ('-created')


class ProductViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = (
        'category', 'category__name', 'category__slug',
        'category__parent__slug', 'category__parent__name', 'name', 'slug',
        'description', 'value'
    )
    search_fields = [
        'category__name', 'category__slug', 'category__parent__slug',
        'category__parent__name', 'name', 'slug', 'description', 'value',
        'category__parent__parent__slug',
        'category__parent__parent__parent__slug',
    ]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    ordering = ('-created')
