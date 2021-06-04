from django.contrib import admin

from .models import OrderProducts, Orders


# Register your models here.
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'webstore',
        'status',
    ]
    search_fields = [
        'webstore',
        'status',
    ]
    

@admin.register(OrderProducts)
class OrderProductsAdmin(admin.ModelAdmin):
    list_display = [
        'products',
        'quantity',
    ]
    search_fields = [
        'products',
        'quantity',
    ]