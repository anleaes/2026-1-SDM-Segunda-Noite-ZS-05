from django.db import models
from usuario.models import Usuario
from leilao.models import Leilao

class Lance(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_lance = models.DateTimeField(auto_now_add=True)
    valido = models.BooleanField(default=True)
    ip_origem = models.CharField(max_length=45, blank=True, null=True)

    leilao = models.ForeignKey(Leilao, on_delete=models.CASCADE, related_name='lances')
    comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='lances_dados')

    class Meta:
        ordering = ['-valor'] # Ordena do maior lance para o menor automaticamente!

    def __str__(self):
        return f'Lance R${self.valor} - {self.comprador.pessoa.nome}'
