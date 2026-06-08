from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)
    vendedor_nome = serializers.CharField(source='vendedor.pessoa.nome', read_only=True)

    class Meta:
        model = Produto
        fields = '__all__'