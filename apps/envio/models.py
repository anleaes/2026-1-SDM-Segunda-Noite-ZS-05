from django.db import models
from pagamento.models import Pagamento

class Envio(models.Model):
    STATUS_CHOICES = [
        ('preparando', 'Preparando para Envio'),
        ('em_transito', 'Em Trânsito'),
        ('entregue', 'Entregue'),
        ('devolvido', 'Devolvido'),
    ]

    codigo_rastreio = models.CharField(max_length=100, blank=True, null=True)
    data_postagem = models.DateTimeField(blank=True, null=True)
    data_entrega = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='preparando')

    # Um pagamento gera um único envio
    pagamento = models.OneToOneField(Pagamento, on_delete=models.CASCADE, related_name='envio')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        rastreio = self.codigo_rastreio if self.codigo_rastreio else "Sem rastreio"
        return f'Envio: {rastreio} - Status: {self.status}'
    