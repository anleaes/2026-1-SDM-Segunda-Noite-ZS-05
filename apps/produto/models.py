from django.db import models
from categoria.models import Categoria
from usuario.models import Usuario

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=2)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='produtos_cadastrados')

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} (Vendedor: {self.vendedor.pessoa.nome})'