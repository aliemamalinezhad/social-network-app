from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
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
