from django.db import models

from .user_model import User
from .movie_model import Movie


class Vote(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_upvote = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"user {self.user.pk} {'up' if self.is_upvote else 'down'}voted '{self.movie}'"
