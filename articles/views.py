from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment
from movies.models import Movie


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_list_create(request):
    if request.method == 'GET':
        serializer = ArticleSerializer(request.user.articles, many=True)
        return Response(serializer.data)
    else:
        movie = Movie.objects.get(pk=request.data['movie_pk'])
        article = Article.objects.create(movie=movie, content=request.data['content'], user=request.user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE', 'GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_update_delete_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            serializer.save(user=request.user)
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response({ 'id': article_pk })
    else:
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
        
        
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': article_pk })


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.like_users.filter(user_id=request.user.id).exists():
        article.like_users.remove(request.user)
        like = False
    else:
        article.like_users.add(request.user)
        like = True
    return Response({ 'like': like, 'like_cnt': article.like_users.count() })