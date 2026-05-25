from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'envios'

router = routers.SimpleRouter()
router.register('', views.EnvioViewSet, basename='envios')

urlpatterns = [
    path('', include(router.urls))
]