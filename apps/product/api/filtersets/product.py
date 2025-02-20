from django_filters.rest_framework import FilterSet, DateFromToRangeFilter, NumberFilter
from apps.product.models import Product


class ProductFilterSet(FilterSet):
    stock_min = NumberFilter(field_name="stock", lookup_expr="gte")
    stock_max = NumberFilter(field_name="stock", lookup_expr="lte")
    value_min = NumberFilter(field_name="value", lookup_expr="gte")
    value_max = NumberFilter(field_name="value", lookup_expr="lte")
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Product
        fields = ["name", "slug", "category", "value", "stock", "created_at"]
