from django.db.models import TextChoices


class GenderChoices(TextChoices):
    MALE = "M", "Masculino"
    FEMALE = "F", "Feminino"
