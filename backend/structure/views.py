from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Structure
from .serializers import StructureSerializer
# from tenant_schemas.utils import get_tenant # Eliminado

class StructureViewSet(viewsets.ModelViewSet):
    serializer_class = StructureSerializer

    def get_queryset(self):
        # tenant = get_tenant(self.request) # Eliminado
        # return Structure.objects.filter(tenant=tenant) # Modificado
        return Structure.objects.all() # Modificado para devolver todos los objetos

    def perform_create(self, serializer):
        # tenant = get_tenant(self.request) # Eliminado
        # serializer.save(tenant=tenant) # Modificado
        serializer.save()

    @action(detail=True, methods=['get'])
    def tree(self, request, pk=None):
        instance = self.get_object()
        # tenant = get_tenant(request) # Eliminado
        children = Structure.objects.filter(
            # tenant=tenant, # Eliminado
            path__startswith=instance.path
        )
        serializer = self.get_serializer(children, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def ancestors(self, request, pk=None):
        instance = self.get_object()
        # tenant = get_tenant(request) # Eliminado
        paths = instance.path.split('/')
        ancestors = Structure.objects.filter(
            # tenant=tenant, # Eliminado
            name__in=paths
        )
        serializer = self.get_serializer(ancestors, many=True)
        return Response(serializer.data)
