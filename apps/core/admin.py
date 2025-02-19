from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group

from apps.core.models import Address


@admin.register(Address)
class AddressAdmin(ModelAdmin):
    list_display = ["street", "city", "state", "zip_code"]
    search_fields = ["street", "city", "state", "zip_code"]
