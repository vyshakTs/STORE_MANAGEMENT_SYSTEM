from django.contrib import admin

from .models import Category, Product, SubCategory


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'net_amount',
        'offer_percentage',
        'status',
    ]
    search_fields = [
        'name',
        'net_amount',
        'offer_percentage',
        'status',
    ]


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]
    search_fields = [
        'title',
    ]


@admin.register(SubCategory)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]
    search_fields = [
        'title',
    ]
