from django.db.models import TextChoices


class StatusChoices(TextChoices):
    ORDERED = "Pedido"
    PAYMENT_PENDING = "Pagamento Pendente"
    PAYMENT_APPROVED = "Pagamento Aprovado"
    PAYMENT_DENIED = "Pagamento Negado"
    PAYMENT_CANCELED = "Pagamento Cancelado"
    PAYMENT_REFUNDED = "Pagamento Reembolsado"
    SHIPPED = "Enviado"
    DELIVERED = "Entregue"
    CANCELED = "Cancelado"
