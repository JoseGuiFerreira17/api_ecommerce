from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db.models import (
    BooleanField,
    CharField,
    EmailField,
    DateField,
    FileField,
    ForeignKey,
    CASCADE,
)
from apps.accounts.choices import GenderChoices
from apps.accounts.managers.managers import UserManager
from apps.core.models import BaseModelMixin


def upload_to(instance, filename):
    return f"profile_images/{instance.pk}/{filename}"


class User(AbstractUser, PermissionsMixin, BaseModelMixin):
    name = CharField("nome de usuário", max_length=255)
    birth_date = DateField("data de nascimento", blank=True, null=True)
    gender = CharField(
        "gênero", max_length=1, choices=GenderChoices.choices, blank=True, null=True
    )
    profile_picture = FileField(
        "foto de perfil", upload_to=upload_to, blank=True, null=True
    )
    email = EmailField("e-mail", unique=True)
    phone = CharField("telefone", max_length=20, blank=True, null=True)
    address = ForeignKey(
        "core.Address",
        verbose_name="endereço",
        on_delete=CASCADE,
        blank=True,
        null=True,
    )

    is_staff = BooleanField(verbose_name="Pode acessar o painel", default=True)
    is_active = BooleanField(verbose_name="ativo", default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"
