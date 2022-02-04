from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    