from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'categories'

router = routers.SimpleRouter()
router.register('', views.CategoriaViewSet, basename='categorias')

urlpatterns = [
    path('', include(router.urls))
]