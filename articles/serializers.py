from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        exclude = ['user',]


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        exclude = ['user', 'article']