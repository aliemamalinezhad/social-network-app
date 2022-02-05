from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import Post
from django.shortcuts import get_object_or_404


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


class UpdatePostApiView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serialized_data = serializers.CreatePostSerializer(instance=post, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DeletePostApiView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(
            {'status':'Item deleted sucessfully'}
            ,status=status.HTTP_204_NO_CONTENT
        )
