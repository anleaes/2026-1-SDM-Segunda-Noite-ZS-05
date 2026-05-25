from django.shortcuts import render
from rest_framework import viewsets
from .models import Avaliacao
from .serializer import AvaliacaoSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer 

    