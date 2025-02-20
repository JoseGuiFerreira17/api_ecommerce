from django.contrib.admin import ModelAdmin


class OrderAdmin(ModelAdmin):
    list_display = ["user", "status", "total"]
    search_fields = ["user__name"]
    list_filter = ["user__name"]
