from .models import Leilao
from rest_framework import serializers

class LeilaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leilao
        fields = '__all__'

        