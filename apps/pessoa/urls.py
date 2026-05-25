from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pessoas'

router = routers.SimpleRouter()
router.register('', views.PessoaViewSet, basename='pessoas')

urlpatterns = [
    path('', include(router.urls))
]