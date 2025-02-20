from django.contrib.admin import site

from apps.purchase.models.cart_item import CartItem
from apps.purchase.admin.cart import CartAdmin
from apps.purchase.admin.order_item import OrderItemAdmin
from apps.purchase.admin.order import OrderAdmin
from apps.purchase.admin.payment import PaymentAdmin

from apps.purchase.admin.cart_item import CartItemAdmin
from apps.purchase.models.cart import Cart
from apps.purchase.models.order_item import OrderItem
from apps.purchase.models.order import Order
from apps.purchase.models.payment import Payment


site.register(CartItem, CartItemAdmin)
site.register(Cart, CartAdmin)
site.register(OrderItem, OrderItemAdmin)
site.register(Order, OrderAdmin)
site.register(Payment, PaymentAdmin)
