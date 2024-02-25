from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from Connect.models import (
    Connect, Contact, Email, Address, Social
)
from Connect.serializer import (
    ConnectSerializer, ConnectAdminSerializer,
    ContactAdminSerializer, EmailAdminSerializer,
    SocialAdminSerializer, AddressAdminSerializer
)

class ConnectViewSet(ModelViewSet):
    queryset = Connect.objects.all()
    serializer_class = ConnectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return ConnectAdminSerializer
        else:
            return ConnectSerializer

    @action(detail=True, methods=['get'])
    def get_contact(self, request, pk=None):
        if request.user.is_authenticated:
            connect = self.get_object()
            contact = connect.contact.all()
            serializer = ContactAdminSerializer(contact, many=True)
            return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_contact(self, request, pk=None):
        if request.user.is_authenticated:
            connect = self.get_object()
            contact = Contact.objects.create(
                primary=request.data['primary'],
                secondary= request.data['secondary'] if 'secondary' in request.data else None
            )
            contact.save()
            connect.contact.add(contact)
            connect.save()
            return Response({'message': 'Contact added successfully', "status":status.HTTP_201_CREATED})

    @action(detail=True, methods=['post'])
    def remove_contact(self, request, pk=None):
        if request.user.is_authenticated:
            connect = self.get_object()
            contact = Contact.objects.get(id=request.data['id'])
            connect.contact.remove(contact)
            connect.save()
            contact.delete()
            return Response({'message': 'Contact removed successfully', "status":status.HTTP_204_NO_CONTENT})

    @action(detail=True, methods=['get'])
    def get_email(self, request, pk=None):
        if request.user.is_authenticated:
            connect = self.get_object()
            email = connect.email.all()
            serializer = EmailAdminSerializer(email, many=True)
            return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_email(self, request, pk=None):
        if request.user.is_authenticated:
            connect = self.get_object()
            email = Email.objects.create(
                name=request.data['name'] if 'name' in request.data else None,
                email=request.data['email']
            )
            email.save()
            connect.email.add(email)
            connect.save()
            return Response({'message': 'Email added successfully', "status":status.HTTP_201_CREATED})

    @action(detail=True, methods=['post'])
    def remove_email(self, request, pk=None):
        if request.user.is_authenticated:
            connect = self.get_object()
            email = Email.objects.get(id=request.data['id'])
            connect.email.remove(email)
            connect.save()
            email.delete()
            return Response({'message': 'Email removed successfully', "status":status.HTTP_204_NO_CONTENT})

    @action(detail=True, methods=['get'])
    def get_address(self, request, pk=None):
        if request.user.is_authenticated:
            connect = self.get_object()
            address = connect.address.all()
            serializer = AddressAdminSerializer(address, many=True)
            return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_address(self, request, pk=None):
        if request.user.is_authenticated:
            connect = self.get_object()
            address = Address.objects.create(
                location=request.data['location'],
                address_line1=request.data['address_line1'],
                address_line2=request.data['address_line2'] if 'address_line2' in request.data else None,
                address_line3=request.data['address_line3'] if 'address_line3' in request.data else None,
            )
            address.save()
            connect.address.add(address)
            connect.save()
            return Response({'message': 'Address added successfully', "status":status.HTTP_201_CREATED})

    @action(detail=True, methods=['post'])
    def remove_address(self, request, pk=None):
        if request.user.is_authenticated:
            connect = self.get_object()
            address = Address.objects.get(id=request.data['id'])
            connect.address.remove(address)
            connect.save()
            address.delete()
            return Response({'message': 'Address removed successfully', "status":status.HTTP_204_NO_CONTENT})

    @action(detail=True, methods=['get'])
    def get_social(self, request, pk=None):
        if request.user.is_authenticated:
            connect = self.get_object()
            social = connect.social.all()
            serializer = SocialAdminSerializer(social, many=True)
            return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_social(self, request, pk=None):
        if request.user.is_authenticated:
            connect = self.get_object()
            social = Social.objects.create(
                name=request.data['name'],
                link=request.data['link']
            )
            social.save()
            connect.social.add(social)
            connect.save()
            return Response({'message': 'Social added successfully', "status":status.HTTP_201_CREATED})

    @action(detail=True, methods=['post'])
    def remove_social(self, request, pk=None):
        if request.user.is_authenticated:
            connect = self.get_object()
            social = Social.objects.get(id=request.data['id'])
            connect.social.remove(social)
            connect.save()
            social.delete()
            return Response({'message': 'Social removed successfully', "status":status.HTTP_204_NO_CONTENT})