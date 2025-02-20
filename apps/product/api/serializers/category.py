from rest_framework.serializers import ModelSerializer
from apps.product.models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        ordering = ["created"]
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "slug": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
        }
