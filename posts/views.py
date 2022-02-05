from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import Post


class PostsApiView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            posts = Post.objects.all().order_by('-created_at')
            serialized_data = serializers.PostsSerializer(posts, many=True).data

            return Response({'data': serialized_data},
                            status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Internal Server Error'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreatePostApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            data = serializers.CreatePostSerializer(data=request.data)
            if data.is_valid():
                data.save()
                return Response({'data': data.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                data.errors,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
