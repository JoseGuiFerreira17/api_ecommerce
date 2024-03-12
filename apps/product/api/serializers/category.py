from rest_framework import serializers
from apps.core.api.serializers import DEFAULT_BASE_FIELDS
from apps.product.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        ordering = ["created"]
        fields = [*DEFAULT_BASE_FIELDS, "name", "slug", "parent"]
        extra_kwargs = {
            "id": {"read_only": True},
            "slug": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
        }
