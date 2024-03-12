from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.product.models import Product
from apps.product.api.serializers import ProductSerializer
from apps.core.api.viewsets import BaseModelViewSet


class ProductViewSet(BaseModelViewSet):
    model = Product
    serializer_class = ProductSerializer
    has_file_field = True

    @action(detail=True, methods=["post"])
    def remove_from_stock(self, request):
        product = self.get_object()
        quantity = request.data.get("quantity", 1)
        if product.stock < quantity:
            return Response(
                {"detail": "Quantidade em estoque insuficiente"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        product.stock -= quantity
        product.save()
        return Response({"stock": product.stock}, status=status.HTTP_200_OK)
