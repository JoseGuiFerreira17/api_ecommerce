from rest_framework import serializers
from apps.core.api.serializers import DEFAULT_BASE_FIELDS
from apps.product.models import Product
from apps.product.api.serializers.category import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        ordering = ["created"]
        fields = [
            *DEFAULT_BASE_FIELDS,
            "category",
            "name",
            "slug",
            "description",
            "value",
            "image",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "slug": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
        }

    def create(self, validated_data):
        category_data = validated_data.pop("category")
        category = CategorySerializer().create(category_data)
        product = Product.objects.create(category=category, **validated_data)
        return product
