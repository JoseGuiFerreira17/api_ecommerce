from django.db.models import (
    OneToOneField,
    CASCADE,
    CharField,
    BooleanField,
    DateTimeField,
)
from apps.core.models import BaseModelMixin
from apps.purchase.choices import PaymentMethodChoices


class Payment(BaseModelMixin):
    order = OneToOneField(
        "Order", verbose_name="pedido", related_name="payment", on_delete=CASCADE
    )
    payment_method = CharField(
        "método de pagamento", choices=PaymentMethodChoices.choices, max_length=25
    )
    paid = BooleanField("pago", default=False)
    paid_at = DateTimeField("pago em", null=True, blank=True)

    class Meta:
        verbose_name = "pagamento"
        verbose_name_plural = "pagamentos"

    def __str__(self):
        return f"Pagamento do pedido {self.order}"
