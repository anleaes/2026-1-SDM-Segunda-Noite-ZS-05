from django.db import models
from produto.models import Produto

class Leilao(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]

    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    valor_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ativo')

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='leiloes')

    class Meta:
        ordering = ['-data_inicio']

    def __str__(self):
        return f'Leilão: {self.produto.nome} ({self.status})'