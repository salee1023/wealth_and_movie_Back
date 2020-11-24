from django.db.models import fields
from rest_framework.serializers import Serializer
from articles.serializers import ArticleSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password',]


class ProfileSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)
    followings = UserSerializer(many=True)
    
    class Meta:
        model = User
        fields = ['username', 'followers', 'followings', 'articles', 'comments',]
