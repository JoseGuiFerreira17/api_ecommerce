import django.contrib.auth.password_validation as validators
from django.core import exceptions

from rest_framework import serializers

from accounts.models import User

MISMATCH = "As senhas não correspondem"


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        ordering = ["created"]
        fields = ["id", "username", "password1", "password2"]
        extra_kwargs = {"id": {"read_only": True}}

    def validate(self, data):
        password = data.get("password1")
        password2 = data.get("password2")

        if password == password2:
            user = User(username=data.get("username"))
            errors = dict()
            try:
                validators.validate_password(password=password, user=user)
            except exceptions.ValidationError as e:
                errors["password1"] = list(e.messages)
                if errors:
                    raise serializers.ValidationError(errors)
        else:
            error_mismatch = {"password1": MISMATCH}
            raise serializers.ValidationError(error_mismatch)

        return super(UserSerializer, self).validate(data)

    def create(self, validated_data):
        password = validated_data.pop("password1")
        user = User(username=validated_data.pop("username"))
        user.is_active = True
        user.is_superuser = False
        user.set_password(password)
        user.save()
        return user


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        ordering = ["created"]
        fields = ["id", "username"]
        extra_kwargs = {"id": {"read_only": True}}
