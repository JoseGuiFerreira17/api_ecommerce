from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from apps.core.api.viewsets import BaseModelViewSet
from apps.purchase.models import Order, Cart
from apps.purchase.choices import StatusChoices
from apps.purchase.api.serializers.order import (
    OrderReadSerializer,
    OrderDetailSerializer,
)


class OrderViewSet(BaseModelViewSet):
    model = Order
    serializer_class = OrderReadSerializer
    action_serializer_classes = {"retrieve": OrderDetailSerializer}

    def create(self, request, *args, **kwargs):
        user = request.user
        cart = get_object_or_404(Cart, user=user)

        total = sum(
            item.product.value * item.quantity for item in cart.cart_items_set.all()
        )

        order = Order.objects.create(
            user=user,
            cart=cart,
            total=total,
            status=StatusChoices.ORDERED,
        )

        cart.active = False
        cart.save()

        return Response(
            self.get_serializer(order).data,
            status=HTTP_201_CREATED,
        )

    @action(detail=True, methods=["PATCH"], url_path="update-status")
    def update_status(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        new_status = request.data.get("status")

        if new_status not in StatusChoices.values:
            return Response(
                {"status": f"Status {new_status} invalid."},
                status=HTTP_400_BAD_REQUEST,
            )

        order.status = new_status
        order.save()

        return Response(self.get_serializer(order).data)
