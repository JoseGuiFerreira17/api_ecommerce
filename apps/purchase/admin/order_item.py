from django.contrib.admin import ModelAdmin


class OrderItemAdmin(ModelAdmin):
    list_display = ["order", "product", "quantity"]
    search_fields = ["order__user__name", "product__name"]
    list_filter = ["order__user__name", "product__name"]
