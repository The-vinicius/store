from django.contrib import admin
from .models import Product, Category, ImageProduct

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created", "modified"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "category",
        "price",
        "is_available",
        "created",
        "modified",
        "offer_available",
        "rebate",
    ]
    list_filter = ["is_available", "created", "modified"]
    list_editable = ["price", "is_available", "offer_available", "rebate"]


@admin.register(ImageProduct)
class ImageAdmin(admin.ModelAdmin):
    pass
