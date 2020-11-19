from django.db import models
from django.conf import settings
from movies.models import Movie


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="articles")
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name="comments", null=True)
    updated_at = models.DateTimeField(auto_now=True)
