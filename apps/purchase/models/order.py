from django.db.models import ForeignKey, CASCADE, CharField, DecimalField, OneToOneField
from apps.core.models import BaseModelMixin
from apps.purchase.choices import StatusChoices


class Order(BaseModelMixin):
    user = ForeignKey(
        "accounts.User",
        verbose_name="usuário",
        related_name="orders",
        on_delete=CASCADE,
    )
    cart = OneToOneField(
        "Cart", verbose_name="carrinho", related_name="orders", on_delete=CASCADE
    )
    status = CharField(
        "status",
        max_length=25,
        choices=StatusChoices.choices,
        default=StatusChoices.ORDERED,
    )
    total = DecimalField("total", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"

    def __str__(self):
        return f"Pedido {self.id} de {self.user}"
