from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True)
    tmdb_id = models.IntegerField(unique=True)
    image_url = models.URLField(max_length=200)
    adult = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title

    def has_long_title(self):
        return len(self.title) > 50
