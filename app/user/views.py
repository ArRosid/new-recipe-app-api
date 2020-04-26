from rest_framework import generics
from .serializers import UserSeializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSeializer
