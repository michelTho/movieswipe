from rest_framework import serializers

from ..models.movie_model import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "image_url", "description", "tmdb_id", "adult"]
