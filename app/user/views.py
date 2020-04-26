from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserSeializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSeializer


class CreateTokenView(ObtainAuthToken):
    """create a new auth token for user"""
    serializer_class = AuthTokenSerializer

    # biar bisa diakses dari browser, kalau endak harus pake postman
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSeializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        """REtrieve and return authenticated user"""
        return self.request.user
