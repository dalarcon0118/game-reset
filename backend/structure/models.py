from django.db import models

class Structure(models.Model):
    NODE_TYPE_CHOICES = [
        ('bank', 'Bank'),
        ('branch', 'Branch'),
        ('zone', 'Zone'),
        ('other', 'Other')
    ]
    
    # tenant = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='structures') # Eliminado
    name = models.CharField(max_length=255)
    node_type = models.CharField(max_length=20, choices=NODE_TYPE_CHOICES, default='branch')
    custom_type = models.CharField(max_length=50, blank=True, help_text='Especifique el tipo cuando seleccione "Other"')
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    level = models.IntegerField(default=0)
    path = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('name', 'parent') # Actualizado: 'tenant' eliminado
        ordering = ['path']

    def __str__(self):
        return self.path
