from django.contrib import admin
from .models import Comment
from import_export.admin import ImportExportModelAdmin

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'product', 'user', 'text', 'created_at')
    search_fields = ('text', 'user__email')
    list_filter = ('created_at',)
