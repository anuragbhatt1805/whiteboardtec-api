from rest_framework import serializers
from Posts.models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating Post"""
    class Meta:
        model = Post
        fields = ('title', 'content',)


class PostListSerializer(serializers.ModelSerializer):
    """Serializer for listing Post"""
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'link',)
        read_only_fields = ('id',)


class PostDetailSerializer(serializers.ModelSerializer):
    """Serializer for detail Post"""
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'link', 'is_active', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'created_at', 'updated_at',)