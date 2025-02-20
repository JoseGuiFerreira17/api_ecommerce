from django_filters.rest_framework import FilterSet
from apps.product.models import Category


class CategoryFilterSet(FilterSet):
    class Meta:
        model = Category
        fields = ["name", "slug"]
