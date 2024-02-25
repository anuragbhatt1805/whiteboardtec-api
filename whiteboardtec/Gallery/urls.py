from rest_framework.routers import DefaultRouter
from django.urls import include, path
from Gallery.views import GalleryViewSet


router = DefaultRouter()
router.register('images', GalleryViewSet, basename='gallery')

urlpatterns = [
    path('', include(router.urls)),
]