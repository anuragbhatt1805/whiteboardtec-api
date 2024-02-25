from rest_framework import serializers
from Career.models import Job, Application

class JobSerializer(serializers.ModelSerializer):
    "Serializer for Job"
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'description': {'required': False},
            'is_active': {'required': False},
        }

class ApplicationSerializer(serializers.ModelSerializer):
    "Serializer for Application"
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'cover_letter': {'required': False},
        }