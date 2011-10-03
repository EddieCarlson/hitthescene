from django.db import models
from genre.models import Genre

class Artist(models.Model):
	name = models.CharField(max_length=80)
	genre = models.ForeignKey(Genre)
