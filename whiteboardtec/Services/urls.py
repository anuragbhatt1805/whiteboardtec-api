from rest_framework.routers import DefaultRouter
from django.urls import include, path
from Services.views import ServiceViewSet


router = DefaultRouter()
router.register('images', ServiceViewSet, basename='services')

urlpatterns = [
    path('', include(router.urls)),
]