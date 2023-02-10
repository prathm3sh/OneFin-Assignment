from .serializers import UserSerializer
from rest_framework import generics

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer