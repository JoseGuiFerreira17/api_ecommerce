from django.urls import path, include

from rest_framework.routers import SimpleRouter

from apps.product.api.viewsets import CategoryViewSet, ProductViewSet


router = SimpleRouter()

router.register("categories", CategoryViewSet, basename="category")
router.register("products", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
]
