from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=200)

    genre = models.CharField(max_length=50)

    language = models.CharField(max_length=50)

    mood = models.CharField(max_length=50)

    companion = models.CharField(max_length=50)

    year_range = models.CharField(max_length=50)

    rating = models.FloatField()

    poster_url = models.TextField(blank=True)

    def __str__(self):
        return self.title