from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from Portfolio.models import Portfolio
from Portfolio.serializer import (
    PortfolioSerializer, PortfolioAdminSerializer,
    ImageAdminSerializer
)


class PortfolioViewSet(ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return PortfolioAdminSerializer
        else:
            return PortfolioSerializer

    @action(detail=True, methods=['post'], url_path='add-image', url_name='add_image')
    def add_image(self, request, pk=None):
        "Add Image to Portfolio"
        portfolio = self.get_object()
        serializer = ImageAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(portfolio=portfolio)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['delete'], url_path='delete-image', url_name='delete_image')
    def delete_image(self, request, pk=None):
        "Delete Image from Portfolio"
        portfolio = self.get_object()
        serializer = ImageAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.delete(portfolio=portfolio)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)