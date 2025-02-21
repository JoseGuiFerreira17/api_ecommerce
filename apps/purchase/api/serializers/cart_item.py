from rest_framework.serializers import ModelSerializer
from apps.purchase.models import CartItem
from apps.product.api.serializers import ProductReadSerializer


class CartItemReadSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"
        extra_kwargs = {
            "cart": {"required": False},
        }


class CartItemDetailSerializer(ModelSerializer):
    product = ProductReadSerializer()

    class Meta:
        model = CartItem
        fields = ["product", "quantity"]
