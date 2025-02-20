from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import ModelSerializer
from apps.product.models import Product
from apps.product.api.serializers.category import CategorySerializer


class ProductCreateSerializer(ModelSerializer):
    image = Base64ImageField(required=False)
    category = CategorySerializer()

    class Meta:
        model = Product
        ordering = ["created"]
        fields = "__all__"
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

    def update(self, instance, validated_data):
        category_data = validated_data.pop("category")
        if category_data:
            if instance.category:
                for key, value in category_data.items():
                    setattr(instance.category, key, value)
                instance.category.save()
            else:
                category = CategorySerializer().create(category_data)
                validated_data["category"] = category
        return super().update(instance, validated_data)


class ProductReadSerializer(ModelSerializer):
    class Meta:
        model = Product
        ordering = ["created"]
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "slug": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
        }


class ProductDetailSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        ordering = ["created"]
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "slug": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
        }
