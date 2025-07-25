from django.contrib import admin
from .models import Brand, Product
from import_export.admin import ImportExportModelAdmin


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'image']
    search_fields = ['name']
    ordering = ['id']


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'category', 'brand', 'price', 'discount', 'quantity', 'is_active']
    list_filter = ['category', 'brand', 'is_active']
    search_fields = ['name', 'description']
    ordering = ['id']
