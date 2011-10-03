from django.db import models
from artist.models import Artist
from venue.models import Venue

class Event(models.Model):
	name = models.CharField(max_length=80)
	date = models.DateTimeField()
	artist = models.ForeignKey(Artist)
	venue = models.ForeignKey(Venue)
	
