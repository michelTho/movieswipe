import random
import threading

from typing import Dict
from rest_framework import views, status
from rest_framework.response import Response
from django.db.models import Max

from ..serializers.movie_serializer import MovieSerializer
from ..models.movie_model import Movie
from ..utils.tmdb_manager import fetch_and_save_random_tmdb_movie


class MovieViewSet(views.APIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request):
        fetch_and_save_random_movie_thread = threading.Thread(
            target=fetch_and_save_random_tmdb_movie
        )
        fetch_and_save_random_movie_thread.start()
        max_movie_pk = Movie.aggregate(max_movie_pk=Max("pk"))["max_movie_pk"]
        while True:
            movie = Movie.filter(pk=random.randint(1, max_movie_pk)).first()
            if movie:
                return Response(movie, status=status.HTTP_200_OK)
