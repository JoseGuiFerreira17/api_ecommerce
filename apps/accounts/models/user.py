from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from apps.accounts.managers.managers import UserManager
from apps.core.models import BaseModelMixin


class User(AbstractUser, PermissionsMixin, BaseModelMixin):
    name = models.CharField("nome de usuário", max_length=255)
    email = models.EmailField("e-mail", unique=True)
    phone = models.CharField("telefone", max_length=20, blank=True, null=True)

    is_staff = models.BooleanField(verbose_name="Pode acessar o painel", default=True)
    is_active = models.BooleanField(verbose_name="ativo", default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"
