from rest_framework.serializers import ModelSerializer
from apps.purchase.models import Cart
from apps.accounts.api.serializers import UserReadSerializer
from apps.purchase.api.serializers import CartItemDetailSerializer


class CartReadSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartDetailSerializer(ModelSerializer):
    user = UserReadSerializer()
    cart_items = CartItemDetailSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "cart_items"]
