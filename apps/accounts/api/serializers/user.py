from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from apps.accounts.models import User
from apps.core.api.serializers import DEFAULT_BASE_FIELDS


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            *DEFAULT_BASE_FIELDS,
            "name",
            "email",
            "phone",
            "is_staff",
            "is_active",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
        }


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
