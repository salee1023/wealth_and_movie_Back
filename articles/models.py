from django.db import models
from django.conf import settings
from movies.models import Movie


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="articles")
    content = models.TextField(blank=True)
    rank = IntegerRangeField(min_value=0, max_value=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name="comments", null=True)
    updated_at = models.DateTimeField(auto_now=True)
