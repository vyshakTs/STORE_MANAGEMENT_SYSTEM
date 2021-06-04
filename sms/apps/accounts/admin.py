from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import City, Country, PostCode, State, User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = [
        'username',
        'email',
        'mobile',
        'user_type',
    ]
    fieldsets = UserAdmin.fieldsets+(
        (None, {'fields': ('user_type', 'mobile'),}),
    )
    # add_fieldsets = UserAdmin.add_fieldsets+(
    #     (None, {'fields': ('user_type', 'mobile'),}),
    # )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = [    
        'name',
        'country_code',
    ]
    search_fields = [
        'name',
        'country_code',
    ]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'state_code',
    ]
    search_fields = [
        'name',
        'state_code',
    ]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'city_code',
    ]
    search_fields = [
        'name',
        'city_code',
    ]


@admin.register(PostCode)
class PostCodeAdmin(admin.ModelAdmin):
    list_display = [
        'city',
        'pin_code',
    ]
    search_fields = [
        'city',
        'pin_code',
    ]
