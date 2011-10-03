from django.db import models
from artist.models import Artist
from venue.models import Venue

class Event(models.Model):
	name = models.CharField(max_length=80)
	date = models.DateTimeField()
	artists = models.ManyToManyField(Artist, null=True)
	venue = models.ForeignKey(Venue, null=True)
	
