from django.db.models import ForeignKey, CASCADE, IntegerField
from apps.core.models import BaseModelMixin


class OrderItem(BaseModelMixin):
    order = ForeignKey("Order", verbose_name="pedido", on_delete=CASCADE)
    product = ForeignKey("product.Product", verbose_name="produto", on_delete=CASCADE)
    quantity = IntegerField("quantidade", default=1)

    class Meta:
        verbose_name = "item do pedido"
        verbose_name_plural = "itens do pedido"

    def __str__(self):
        return f"{self.order.user} - {self.product} - {self.quantity}"
