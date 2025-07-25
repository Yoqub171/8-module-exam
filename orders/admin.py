from django.contrib import admin
from .models import Order, OrderItem
from import_export.admin import ImportExportModelAdmin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("price",)
    autocomplete_fields = ("product",)


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ("id", "user", "full_name", "status", "total_price", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__email", "full_name", "phone")
    readonly_fields = ("total_price", "created_at")
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(ImportExportModelAdmin):
    list_display = ("id", "order", "product", "quantity", "price")
    list_filter = ("product",)
    search_fields = ("product__name", "order__user__email")
    autocomplete_fields = ("product", "order")
