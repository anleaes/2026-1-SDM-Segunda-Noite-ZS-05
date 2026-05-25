from .models import Lance
from rest_framework import serializers

class LanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lance
        fields = '__all__'