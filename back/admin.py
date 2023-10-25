from django.contrib import admin

from back.models.movie_model import Movie
from back.models.vote_model import Vote
from back.models.user_model import User

admin.site.register(Movie)
admin.site.register(Vote)
admin.site.register(User)
