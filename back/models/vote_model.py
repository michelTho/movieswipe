from django.db import models

from .movie_model import Movie


class Vote(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_upvote = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{'up' if self.is_upvote else 'down'}voted '{self.movie}'"
