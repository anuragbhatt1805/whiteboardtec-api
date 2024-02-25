from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from Portfolio.models import Portfolio, Image
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

    @action(detail=True, methods=['get'])
    def get_image(self, request, pk=None):
        if request.user.is_authenticated:
            portfolio = self.get_object()
            image = portfolio.image.all()
            serializer = ImageAdminSerializer(image, many=True)
            return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_image(self, request, pk=None):
        if request.user.is_authenticated:
            portfolio = self.get_object()
            serializer = ImageAdminSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(portfolio=portfolio)
            return Response({'message': 'Image added successfully', "status":status.HTTP_201_CREATED})

    @action(detail=True, methods=['post'])
    def remove_image(self, request, pk=None):
        if request.user.is_authenticated:
            portfolio = self.get_object()
            image = Image.objects.get(id=request.data['id'])
            portfolio.image.remove(image)
            portfolio.save()
            image.delete()
            return Response({'message': 'Image removed successfully', "status":status.HTTP_204_NO_CONTENT})