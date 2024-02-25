from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from Gallery.models import Gallery
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from Gallery.serializer import (
    GalleryCreateSerializer,
    GalleryListSerializer,
)


class GalleryViewSet(ModelViewSet):
    """Handle creating and updating Gallery"""
    queryset = Gallery.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'create':
            return GalleryCreateSerializer
        return GalleryListSerializer
