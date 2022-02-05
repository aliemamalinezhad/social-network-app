from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Post


class PostsSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'text', 'created_at', 'updated_at', 'author']


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
