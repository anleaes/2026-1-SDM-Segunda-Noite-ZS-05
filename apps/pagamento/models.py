from django.db import models
from leilao.models import Leilao

class Pagamento(models.Model):
    METODO_CHOICES = [
        ('pix', 'PIX'),
        ('boleto', 'Boleto Bancário'),
        ('cartao', 'Cartão de Crédito'),
    ]

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('recusado', 'Recusado'),
    ]

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    metodo = models.CharField(max_length=20, choices=METODO_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    leilao = models.OneToOneField(Leilao, on_delete=models.CASCADE, related_name='pagamento')

    class Meta:
        ordering = ['-data_pagamento']

    def __str__(self):
        return f'Pagamento R${self.valor} - Leilão: {self.leilao.id} ({self.status})'