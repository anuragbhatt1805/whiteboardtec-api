from rest_framework import serializers
from Portfolio.models import (
    Portfolio, Image
)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['caption', 'image',]

class ImageAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        read_only_fields = ['id', 'created_at',]
        extra_kwargs = {
            'caption': {'required': False},
        }

    def save(self, portfolio, **kwargs):
        image = Image.objects.create(
            caption=self.validated_data['caption'] if 'caption' in self.validated_data else None,
            image=self.validated_data['image']
        )
        image.save()
        portfolio.image.add(image)
        portfolio.save()
        return image


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['title', 'description', 'image', 'document',]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        image = [
            ImageSerializer(id=image).data for image in response['image']
        ]
        response['image'] = image
        return response

class PortfolioAdminSerializer(serializers.ModelSerializer):
    image = ImageAdminSerializer(many=True, required=False)
    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'description', 'image', 'document', 'created_at', 'updated_at',]
        read_only_fields = ['id', 'created_at', 'updated_at',]
        extra_kwargs = {
            'image': {'required': False},
            'document': {'required': False},
        }