from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_204_NO_CONTENT
from django.shortcuts import get_object_or_404

from apps.core.api.viewsets import BaseModelViewSet
from apps.purchase.models import Cart, CartItem
from apps.product.models import Product
from apps.purchase.api.serializers.cart import CartReadSerializer, CartDetailSerializer
from apps.purchase.api.serializers.cart_item import CartItemReadSerializer


class CartViewSet(BaseModelViewSet):
    model = Cart
    serializer_class = CartReadSerializer
    action_serializer_classes = {
        "retrieve": CartDetailSerializer,
        "add_product": CartItemReadSerializer,
    }

    @action(detail=True, methods=["POST"], url_path="add-products")
    def add_product(self, request, pk=None):
        user = request.user
        cart = self.model.objects.get_or_create(user=user, active=True)[0]

        if not cart.active:
            cart = Cart.objects.create(user=user, active=True)

        product_id = request.data.get("product")
        quantity = request.data.get("quantity", 1)

        product = get_object_or_404(Product, id=product_id)

        if product.stock < quantity:
            return Response(
                {"message": "Product out of stock"}, status=HTTP_400_BAD_REQUEST
            )

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        if cart_item.product.stock > product.stock:
            return Response(
                {"message": "Product out of stock"}, status=HTTP_400_BAD_REQUEST
            )

        cart_item.save()

        return Response(
            {"message": "Product added to cart successfully"}, status=HTTP_200_OK
        )

    @action(detail=True, methods=["delete"])
    def remove_product(self, request, pk=None):
        user = request.user
        cart = get_object_or_404(Cart, pk=pk, active=True, user=user)

        product_id = request.data.get("product")
        product = get_object_or_404(Product, id=product_id)

        cart_item = get_object_or_404(CartItem, cart=cart, product=product)
        cart_item.delete()

        return Response(
            {"message": "Product removed from cart successfully"},
            status=HTTP_204_NO_CONTENT,
        )

    @action(detail=False, methods=["delete"])
    def clean(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user, active=True).first()
        cart_items = CartItem.objects.filter(cart=cart)
        cart_items.delete()

        return Response(
            {"message": "Cart cleaned successfully"}, status=HTTP_204_NO_CONTENT
        )
