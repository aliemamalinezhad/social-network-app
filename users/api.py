from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView

User = get_user_model()


class RegisterApi(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "messages": "User Created Successfully.  Now perform Login to get your token",
        },
            status=status.HTTP_200_OK)


class GetUsers(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
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
                })

            return Response({'data': users},
                            status=status.HTTP_200_OK)
        except:
            return Response({'data': 'Internal server error'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
