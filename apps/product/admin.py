from django.contrib import admin
from product.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "parent"]
    fieldsets = [["", {"fields": ["name", "parent"]}]]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "category", "value"]
    fieldsets = [
        ["", {"fields": ["name", "category", "description", "value", "image"]}]
    ]
