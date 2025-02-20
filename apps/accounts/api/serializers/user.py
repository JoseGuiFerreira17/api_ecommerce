from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from apps.accounts.models import User
from apps.core.models import Address
from apps.core.api.serializers import AddressSerializer


class UserReadSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ["password", "groups", "user_permissions"]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
        }


class UserDetailSerializer(ModelSerializer):
    profile_picture = Base64ImageField(required=False)
    address = AddressSerializer(required=False)

    class Meta:
        model = User
        exclude = ["password", "groups", "user_permissions"]

    def update(self, instance, validated_data):
        address_data = validated_data.pop("address", None)
        if address_data:
            if instance.address:
                for key, value in address_data.items():
                    setattr(instance.address, key, value)
                instance.address.save()
            else:
                address = Address.objects.create(**address_data)
                validated_data["address"] = address
        return super().update(instance, validated_data)


class UserCreateSerializer(ModelSerializer):
    profile_picture = Base64ImageField(required=False)
    password = CharField(write_only=True)
    password_confirmation = CharField(write_only=True)

    class Meta:
        model = User
        exclude = ["groups", "user_permissions"]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
            "is_superuser": {"read_only": True},
        }

    def validate(self, data):
        if data["password"] != data.pop("confirm_password"):
            raise ValidationError("As senhas não conferem")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserUpdatePasswordSerializer(ModelSerializer):
    password = CharField(write_only=True)
    password_confirmation = CharField(write_only=True)
    last_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ["password", "password_confirmation", "last_password"]

    def validate(self, data):
        user = self.instance
        if not user.check_password(data["last_password"]):
            raise ValidationError("Senha atual incorreta")

        if data["password"] != data["password_confirmation"]:
            raise ValidationError("As senhas não conferem")
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
