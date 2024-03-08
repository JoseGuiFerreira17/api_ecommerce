from django.urls import path, include
from rest_framework import routers
from product import views

app_name = 'product'

router = routers.DefaultRouter()

router.register('category', views.CategoryViewSet, basename='category')
router.register('product', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]