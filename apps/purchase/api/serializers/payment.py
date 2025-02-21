from rest_framework.serializers import ModelSerializer
from apps.purchase.models import Payment
from apps.purchase.api.serializers.order import OrderReadSerializer


class PaymentReadSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class PaymentDetailSerializer(ModelSerializer):
    order = OrderReadSerializer()

    class Meta:
        model = Payment
        fields = "__all__"
