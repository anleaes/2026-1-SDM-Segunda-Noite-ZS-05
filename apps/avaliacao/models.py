from django.db import models
from usuario.models import Usuario
from leilao.models import Leilao

class Avaliacao(models.Model):
    nota = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    leilao = models.ForeignKey(Leilao, on_delete=models.CASCADE, related_name='avaliacoes')
    avaliador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='avaliacoes_feitas')

    class Meta:
        ordering = ['-data_avaliacao'] # Ordena das avaliações mais recentes para as mais antigas

    def __str__(self):
        return f'Avaliação {self.nota} estrelas - {self.avaliador.pessoa.nome}'