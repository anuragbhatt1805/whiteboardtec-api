from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from Services.models import ServiceImage
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from Services.serializer import (
    ServiceCreateSerializer,
    ServiceListSerializer,
)


class ServiceViewSet(ModelViewSet):
    """Handle creating and updating Service"""
    queryset = ServiceImage.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'create':
            return ServiceCreateSerializer
        return ServiceListSerializer
