from rest_framework import serializers
from .models import Structure

class StructureSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Structure
        fields = ['id', 'name', 'description', 'parent', 'level', 'path', 'children', 'created_at', 'updated_at']
        # read_only_fields = ['level', 'path', 'tenant'] # Modificado
        read_only_fields = ['level', 'path'] # 'tenant' eliminado

    def get_children(self, obj):
        # children = Structure.objects.filter(parent=obj, tenant=obj.tenant) # Modificado
        children = Structure.objects.filter(parent=obj) # 'tenant' eliminado
        return StructureSerializer(children, many=True).data