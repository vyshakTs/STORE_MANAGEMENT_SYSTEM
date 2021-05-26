from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import WebStore


# Register your models here.
@admin.register(WebStore)
class WebStoreAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'name',
        'city',
        'phone_no',
    ]
    search_fields = [
        'user',
        'name',
        'city',
        'phone_no',
    ]
