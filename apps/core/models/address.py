from django.db.models import CharField
from apps.core.choices import StatesChoices
from apps.core.models import BaseModelMixin


class Address(BaseModelMixin):
    street = CharField("rua", max_length=255)
    number = CharField("número", max_length=10)
    complement = CharField("complemento", max_length=255, blank=True, null=True)
    neighborhood = CharField("bairro", max_length=255)
    city = CharField("cidade", max_length=255)
    state = CharField("estado", choices=StatesChoices, max_length=2)
    zip_code = CharField("CEP", max_length=9)

    def __str__(self):
        return f"{self.street}, {self.number} - {self.city}/{self.state}"

    class Meta:
        verbose_name = "endereço"
        verbose_name_plural = "endereços"
