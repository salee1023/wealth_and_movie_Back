from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    description = models.TextField(blank=True)
    profile = models.URLField("Profile URL", blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')