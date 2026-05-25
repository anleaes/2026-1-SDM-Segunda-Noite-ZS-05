from django.db import models
from pessoa.models import Pessoa

class Usuario(models.Model):
    PERFIL_CHOICES = [
        ('comprador', 'Comprador'),
        ('vendedor', 'Vendedor'),
        ('admin', 'Administrador'),
    ]

    ativo = models.BooleanField(default=True)
    pontuacao = models.IntegerField(default=0)
    cpf = models.CharField(max_length=14, unique=True)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'Usuario: {self.pessoa.nome} - {self.perfil}'