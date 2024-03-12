from apps.product.models import Category
from apps.product.api.serializers import CategorySerializer
from apps.core.api.viewsets import BaseModelViewSet


class CategoryViewSet(BaseModelViewSet):
    model = Category
    serializer_class = CategorySerializer
