from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'produtos'

router = routers.SimpleRouter()
router.register('', views.ProdutoViewSet, basename='produtos')

urlpatterns = [
    path('', include(router.urls))
]