from rest_framework.serializers import ModelSerializer
from apps.purchase.models import Order
from apps.accounts.api.serializers import UserReadSerializer


class OrderReadSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderDetailSerializer(ModelSerializer):
    user = UserReadSerializer()

    class Meta:
        model = Order
        fields = "__all__"
