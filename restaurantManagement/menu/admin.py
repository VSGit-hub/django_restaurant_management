from django.contrib import admin
from .models import ItemCategory, MenuItem

@admin.register(ItemCategory)
class RegisterItemCategory(admin.ModelAdmin):
    list_display = ['category_name']

@admin.register(MenuItem)
class RegisterMenuItem(admin.ModelAdmin):
    list_display = ['item_name', 'item_category', 'item_price', ]
    search_fields = ['item_name', 'item_category']
    list_filter = ['item_category', 'is_available']
