from django.contrib import admin
from .models import Role, UserRole

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'assigned_at', 'is_active')
    list_filter = ('is_active', 'role', 'assigned_at')
    search_fields = ('user__username', 'role__name')
    raw_id_fields = ('user', 'role')
    readonly_fields = ('assigned_at',)
    ordering = ('-assigned_at',)
