from django.contrib import admin
from .models import Category
from import_export.admin import ImportExportModelAdmin


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    ordering = ['id']
