from typing import Dict
from django.shortcuts import get_object_or_404, render
from rest_framework import views, status
from rest_framework.response import Response

from ..serializers.movie_serializer import MovieSerializer
from ..models.movie_model import Movie
from ..utils.tmdb_manager import get_random_tmdb_movie


class MovieViewSet(views.APIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request):
        movie: Dict = get_random_tmdb_movie()
        serializer = MovieSerializer(data=movie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
