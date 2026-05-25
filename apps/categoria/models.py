from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    codigo_setor = models.IntegerField()
    destaque = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.nome}'