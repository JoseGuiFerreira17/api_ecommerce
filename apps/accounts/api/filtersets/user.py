from django_filters.rest_framework import FilterSet, CharFilter
from apps.accounts.models import User
from apps.accounts.choices import GenderChoices


class UserFilterSet(FilterSet):
    gender = CharFilter(field_name="gender", lookup_expr="exact", choices=GenderChoices)
    state = CharFilter(
        field_name="address__state", lookup_expr="iexact", label="Estado"
    )
    city = CharFilter(field_name="address__city", lookup_expr="iexact", label="Cidade")

    class Meta:
        model = User
        fields = ["name", "email", "birth_date", "phone", "gender", "state", "city"]
