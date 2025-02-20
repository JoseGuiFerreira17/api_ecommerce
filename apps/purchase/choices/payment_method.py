from django.db.models import TextChoices


class PaymentMethodChoices(TextChoices):
    CREDIT_CARD = "Cartão de Crédito", "Cartão de Crédito"
    BOLETO = "Boleto", "Boleto"
    PIX = "PIX", "PIX"
    TRANSFER = "Transferência", "Transferência"
    DEBIT_CARD = "Cartão de Débito", "Cartão de Débito"
