from typing import Dict
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # genres = serializers.ReadOnlyField(source='genre.name')

    class Meta:
        model = Movie
        fields = '__all__'