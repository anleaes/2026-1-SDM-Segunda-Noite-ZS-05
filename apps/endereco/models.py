from django.db import models
from usuario.models import Usuario

class Endereco(models.Model):
    cep = models.CharField(max_length=10)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=150, blank=True, null=True)
    principal = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='enderecos')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.cep} - {self.numero} (Usuario: {self.usuario.pessoa.nome})'
    
    