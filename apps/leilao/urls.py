from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'leiloes'

router = routers.SimpleRouter()
router.register('', views.LeilaoViewSet, basename='leiloes')

urlpatterns = [
    path('', include(router.urls))
]