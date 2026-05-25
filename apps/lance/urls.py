from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'lances'

router = routers.SimpleRouter()
router.register('', views.LanceViewSet, basename='lances')

urlpatterns = [
    path('', include(router.urls))
]