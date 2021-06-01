from django.contrib import admin
from .models import Product

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