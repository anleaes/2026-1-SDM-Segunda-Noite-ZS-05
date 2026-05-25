from django.shortcuts import render
from rest_framework import viewsets
from .models import Leilao
from .serializer import LeilaoSerializer

class LeilaoViewSet(viewsets.ModelViewSet):
    queryset = Leilao.objects.all()
    serializer_class = LeilaoSerializer