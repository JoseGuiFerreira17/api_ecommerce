from apps.product.models import Product
from apps.product.api.serializers import ProductSerializer
from apps.core.api.viewsets import BaseModelViewSet


class ProductViewSet(BaseModelViewSet):
    model = Product
    serializer_class = ProductSerializer
    has_file_field = True
