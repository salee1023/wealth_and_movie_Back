from typing import Dict
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_genres(self, obj):
        return 