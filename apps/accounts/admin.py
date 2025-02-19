from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from apps.accounts.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["name", "email", "birth_date", "is_active", "is_staff"]
    list_filter = ["is_active", "is_staff"]
    search_fields = ["name", "email"]

    fieldsets = [
        [
            "Informações pessoais",
            {
                "fields": [
                    "name",
                    "birth_date",
                    "gender",
                    "phone",
                    "email",
                    "address",
                    "profile_picture",
                ]
            },
        ],
        [
            "Dados de acesso",
            {
                "fields": [
                    "password",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ]
            },
        ],
    ]
    add_fieldsets = [["Informações pessoais", {"fields": ["password1", "password2"]}]]
