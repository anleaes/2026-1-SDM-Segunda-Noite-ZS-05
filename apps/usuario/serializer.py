from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    # Estas duas linhas fazem a mágica de buscar o nome na tabela Pessoa buscando pela FK
    pessoa_nome = serializers.CharField(source='pessoa.nome', read_only=True)
    pessoa_sobrenome = serializers.CharField(source='pessoa.sobrenome', read_only=True)

    class Meta:
        model = Usuario
        fields = '__all__' # Mantém o __all__ para trazer o CPF, perfil, ativo, etc.