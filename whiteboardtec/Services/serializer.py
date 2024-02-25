from rest_framework import serializers
from Services.models import ServiceImage


class ServiceCreateSerializer(serializers.ModelSerializer):
    """Serializer for ServiceImage object"""

    class Meta:
        model = ServiceImage
        fields = ['caption', 'image']
        extra_kwargs = {
            'caption': {'required': False}
        }

class ServiceListSerializer(serializers.ModelSerializer):
    """Serializer for ServiceImage object"""

    class Meta:
        model = ServiceImage
        fields = ['id', 'caption', 'image']