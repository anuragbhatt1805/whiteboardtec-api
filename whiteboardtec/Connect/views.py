from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from Connect.models import (
    Connect, Contact, Email, Address, Social
)
from Connect.serializer import (
    ConnectSerializer, ConnectAdminSerializer,
    ContactAdminSerializer,
    EmailAdminSerializer,
    AddressAdminSerializer,
    SocialAdminSerializer
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

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactAdminSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class EmailViewSet(ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailAdminSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressAdminSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class SocialViewSet(ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialAdminSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]