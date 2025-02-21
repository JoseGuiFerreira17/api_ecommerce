from django.urls import path, include

from rest_framework.routers import SimpleRouter

from apps.purchase.api.viewsets import CartViewSet, OrderViewSet, PaymentViewSet

router = SimpleRouter()

router.register("carts", CartViewSet, basename="cart")
router.register("orders", OrderViewSet, basename="order")
router.register("payments", PaymentViewSet, basename="payment")


urlpatterns = [
    path("", include(router.urls)),
]
