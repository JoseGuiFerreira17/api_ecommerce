from django.contrib.admin import ModelAdmin


class CartItemAdmin(ModelAdmin):
    list_display = ["cart", "product", "quantity"]
    search_fields = ["cart__user__name", "product__name"]
    list_filter = ["cart__user__name", "product__name"]
