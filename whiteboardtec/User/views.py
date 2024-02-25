from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from User.models import UserModel
from User.serializer import UserSerializer
from User.permissions import UserPermissions


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user Authentication Token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserViewSet(ModelViewSet):
    """Handle creating and updating user"""
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, UserPermissions,)

    def get_queryset(self):
        user = self.request.user
        return UserModel.objects.filter(id=user.id)
