from rest_framework import serializers
from User.models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'username', 'password', 'name', 'email', 'role', 'phone',
        ]
        extra_kwargs = {
            'username': {'read_only': True},
            'password': {
                    'write_only': True,
                    'style': {'input_type': 'password'}
                },
        }

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)