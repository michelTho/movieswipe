from django.db import models


class AppUser(models.Model):
    session_id = models.CharField(max_length=200)

    def __str__(self):
        return self.session_id
