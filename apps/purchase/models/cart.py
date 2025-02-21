from django.db.models import ForeignKey, CASCADE, BooleanField
from apps.core.models import BaseModelMixin


class Cart(BaseModelMixin):
    user = ForeignKey("accounts.User", verbose_name="usuário", on_delete=CASCADE)
    active = BooleanField("ativo", default=True)

    class Meta:
        verbose_name = "carrinho"
        verbose_name_plural = "carrinhos"

    def __str__(self):
        return f"Carrinho de {self.user}"
