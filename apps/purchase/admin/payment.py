from django.contrib.admin import ModelAdmin


class PaymentAdmin(ModelAdmin):
    list_display = ["order", "payment_method", "paid", "paid_at"]
    search_fields = ["order__user__name", "payment_method"]
    list_filter = ["order__user__name", "payment_method", "paid", "paid_at"]
