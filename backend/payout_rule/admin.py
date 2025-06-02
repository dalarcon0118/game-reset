from django.contrib import admin
from .models import PayoutRule

@admin.register(PayoutRule)
class PayoutRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'game_type', 'payout_rate', 'condition', 'owner_structure', 'is_active', 'created_at')
    list_filter = ('game_type', 'owner_structure', 'is_active', 'created_at')
    search_fields = ('game_type__name', 'owner_structure__name', 'condition')
    raw_id_fields = ('game_type', 'owner_structure')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('game_type', '-created_at')
