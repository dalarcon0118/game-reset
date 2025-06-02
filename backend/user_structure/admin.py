from django.contrib import admin
from .models import UserStructure

@admin.register(UserStructure)
class UserStructureAdmin(admin.ModelAdmin):
    list_display = ('user', 'structure', 'role', 'is_active', 'assigned_at')
    list_filter = ('is_active', 'role', 'assigned_at')
    search_fields = ('user__username', 'structure__name', 'role')
    raw_id_fields = ('user', 'structure')
    readonly_fields = ('assigned_at',)
    ordering = ('-assigned_at',)
