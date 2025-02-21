from django.db.models import ForeignKey, CASCADE, IntegerField
from apps.core.models import BaseModelMixin


class CartItem(BaseModelMixin):
    cart = ForeignKey(
        "Cart", verbose_name="carrinho", related_name="cart_items", on_delete=CASCADE
    )
    product = ForeignKey("product.Product", verbose_name="produto", on_delete=CASCADE)
    quantity = IntegerField("quantidade", null=True, blank=True)

    class Meta:
        verbose_name = "item do carrinho"
        verbose_name_plural = "itens do carrinho"

    def __str__(self):
        return f"{self.cart.user} - {self.product} - {self.quantity}"
