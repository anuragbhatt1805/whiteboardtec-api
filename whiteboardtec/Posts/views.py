from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from Posts.models import Post
from Posts.serializer import (
    PostCreateSerializer,
    PostListSerializer,
    PostDetailSerializer,
)

class PostViewSet(ModelViewSet):
    """ViewSet for Post"""
    queryset = Post.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content', 'link']

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        elif self.action == 'list':
            if self.request.user.is_authenticated:
                return PostDetailSerializer
            else:
                return PostListSerializer
        else:
            return PostDetailSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.all()
        else:
            return Post.objects.filter(is_active=True)