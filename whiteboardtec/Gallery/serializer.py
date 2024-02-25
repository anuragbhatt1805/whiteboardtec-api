from rest_framework import serializers
from Gallery.models import Gallery


class GalleryCreateSerializer(serializers.ModelSerializer):
    """Serializer for GalleryImage object"""

    class Meta:
        model = Gallery
        fields = ['caption', 'image']
        extra_kwargs = {
            'caption': {'required': False}
        }

class GalleryListSerializer(serializers.ModelSerializer):
    """Serializer for GalleryImage object"""

    class Meta:
        model = Gallery
        fields = ['id', 'caption', 'image']