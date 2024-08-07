from rest_framework.routers import DefaultRouter
from django.urls import include, path
from Connect.views import (
    ConnectViewSet,
)

router = DefaultRouter()
router.register('connect', ConnectViewSet, basename='connect')

urlpatterns = [
    path('', include(router.urls)),
]