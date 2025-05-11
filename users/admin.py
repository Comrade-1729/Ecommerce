from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1

class CustomUserAdmin(UserAdmin):
    inlines = [AddressInline]

admin.site.register(User, CustomUserAdmin)