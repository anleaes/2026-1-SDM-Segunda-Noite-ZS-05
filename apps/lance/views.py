from django.shortcuts import render
from rest_framework import viewsets
from .models import Lance
from .serializer import LanceSerializer

class LanceViewSet(viewsets.ModelViewSet):
    queryset = Lance.objects.all()
    serializer_class = LanceSerializer

    