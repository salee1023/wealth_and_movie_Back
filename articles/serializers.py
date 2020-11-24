from movies.serializers import MovieSerializer
from rest_framework import serializers
from movies.serializers import MovieSerializer
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    created_at = serializers.DateTimeField(format="%Y-%m-%d")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Comment
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    movie = MovieSerializer()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = "__all__"

