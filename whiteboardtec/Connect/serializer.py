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

    class Meta:
        model = Connect
        fields = ['contact', 'email', 'address', 'social']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        contact = []
        email = []
        address = []
        social = []
        for item in representation['contact']:
            contact.append(ContactSerializer(Contact.objects.get(id=item)).data)
        for item in representation['email']:
            email.append(EmailSerializer(Email.objects.get(id=item)).data)
        for item in representation['address']:
            address.append(AddressSerializer(Address.objects.get(id=item)).data)
        for item in representation['social']:
            social.append(SocialSerializer(Social.objects.get(id=item)).data)
        representation['contact'] = contact
        representation['email'] = email
        representation['address'] = address
        representation['social'] = social
        return representation

class ConnectAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Connect
        fields = '__all__'
        read_only_fields = ['id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        contact = []
        email = []
        address = []
        social = []
        for item in representation['contact']:
            contact.append(ContactAdminSerializer(Contact.objects.get(id=item)).data)
        for item in representation['email']:
            email.append(EmailAdminSerializer(Email.objects.get(id=item)).data)
        for item in representation['address']:
            address.append(AddressAdminSerializer(Address.objects.get(id=item)).data)
        for item in representation['social']:
            social.append(SocialAdminSerializer(Social.objects.get(id=item)).data)
        representation['contact'] = contact
        representation['email'] = email
        representation['address'] = address
        representation['social'] = social
        return representation