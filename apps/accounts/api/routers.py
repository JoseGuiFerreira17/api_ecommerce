from django.urls import path, include

from rest_framework.routers import SimpleRouter

from apps.accounts.api.viewsets import UserViewSet

router = SimpleRouter()

router.register("users", UserViewSet, basename="user")

urlpatterns = [path("", include(router.urls))]
