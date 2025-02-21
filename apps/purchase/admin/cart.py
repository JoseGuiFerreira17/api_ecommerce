from django.contrib.admin import ModelAdmin


class CartAdmin(ModelAdmin):
    list_display = ["user", "created_at"]
    search_fields = ["user__name"]
    list_filter = ["user__name"]
