from rest_framework import serializers
from Connect.models import (
    Contact,
    Email,
    Address,
    Social,
    Connect
)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['primary', 'secondary']

class ContactAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['id']

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['name', 'email']

class EmailAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'
        read_only_fields = ['id']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['location', 'address_line1', 'address_line2', 'address_line3']

class AddressAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ['id']

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['name', 'link']

class SocialAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
        read_only_fields = ['id']

class ConnectSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(many=True, required=False)
    email = EmailSerializer(many=True, required=False)
    address = AddressSerializer(many=True, required=False)
    social = SocialSerializer(many=True, required=False)

    class Meta:
        model = Connect
        fields = ['contact', 'email', 'address', 'social']
        

class ConnectAdminSerializer(serializers.ModelSerializer):
    contact = ContactAdminSerializer(many=True, required=False)
    email = EmailAdminSerializer(many=True, required=False)
    address = AddressAdminSerializer(many=True, required=False)
    social = SocialAdminSerializer(many=True, required=False)
    class Meta:
        model = Connect
        fields = '__all__'
        read_only_fields = ['id']