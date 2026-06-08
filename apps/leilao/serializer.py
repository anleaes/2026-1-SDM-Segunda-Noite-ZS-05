from rest_framework import serializers
from .models import Leilao

class LeilaoSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)

    class Meta:
        model = Leilao
        fields = '__all__'