from django.contrib import admin
from .models import Structure

@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'node_type', 'parent', 'path', 'custom_type', 'created_at', 'updated_at')
    list_filter = ('node_type', 'custom_type', 'created_at', 'updated_at')
    search_fields = ['name', 'description', 'path', 'custom_type']
    raw_id_fields = ('parent',)
    ordering = ('path',)

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'node_type', 'parent', 'custom_type')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('path', 'created_at', 'updated_at')

    def get_queryset(self, request):
        return Structure.objects.prefetch_related('children')
