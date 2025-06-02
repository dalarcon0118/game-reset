from django.contrib import admin
from .models import Origin

@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('code', 'name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)
    list_display_links = ('code', 'name')
