from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from apps.core.api.viewsets import BaseModelViewSet
from apps.purchase.models import Payment, Order

from apps.purchase.choices import PaymentMethodChoices, StatusChoices
from apps.purchase.api.serializers.payment import (
    PaymentReadSerializer,
    PaymentDetailSerializer,
)


class PaymentViewSet(BaseModelViewSet):
    model = Payment
    serializer_class = PaymentReadSerializer
    action_serializer_classes = {"retrieve": PaymentDetailSerializer}

    def create(self, request, *args, **kwargs):
        order = Order.objects.get(pk=request.data.get("order"))
        payment_method = request.data.get("payment_method")

        if payment_method not in PaymentMethodChoices.values:
            return Response(
                {"payment_method": f"Payment method {payment_method} invalid."},
                status=HTTP_400_BAD_REQUEST,
            )

        payment = Payment.objects.create(
            order=order,
            payment_method=payment_method,
        )

        order.status = StatusChoices.PAYMENT_PENDING
        order.save()

        return Response(
            self.get_serializer(payment).data,
            status=HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        payment = self.get_object()
        payment_method = request.data.get("payment_method")

        if payment.paid:
            return Response(
                {"payment": "Payment already paid."}, status=HTTP_400_BAD_REQUEST
            )

        if payment_method not in PaymentMethodChoices.values:
            return Response(
                {"payment_method": f"Payment method {payment_method} invalid."},
                status=HTTP_400_BAD_REQUEST,
            )

        payment.payment_method = payment_method
        payment.save()

        return Response(self.get_serializer(payment).data)

    @action(detail=True, methods=["PATCH"], url_path="pay")
    def pay(self, request, pk=None):
        payment = self.get_object()

        if payment.paid:
            return Response(
                {"payment": "Payment already paid."}, status=HTTP_400_BAD_REQUEST
            )

        payment.paid = True
        payment.save()

        return Response(self.get_serializer(payment).data)

    @action(detail=True, methods=["PATCH"], url_path="cancel")
    def cancel(self, request, pk=None):
        payment = self.get_object()

        if payment.paid:
            return Response(
                {"payment": "Payment already paid."}, status=HTTP_400_BAD_REQUEST
            )
        payment.order.status = StatusChoices.PAYMENT_CANCELED
        payment.delete()

        return Response(status=HTTP_204_NO_CONTENT)
