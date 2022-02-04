from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView

User = get_user_model()


class UsersService:
    def get_users_service(self):
        users = []
        all_users = User.objects.all()
        for user in all_users:
            users.append({
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': user.phone,
                'password': user.password,
                'is_staff': user.is_staff,
                'date_joined': user.date_joined,
            })
        return users