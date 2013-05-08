from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Platform(models.Model):
	name = models.CharField(max_length=255, unique=True)
	platform_id = models.IntegerField()
	alias = models.CharField(max_length=255, blank=True)
	
	def __unicode__(self):
		return u'%s'%self.name

class Genre(models.Model):
	name = models.CharField(max_length=255, unique=True)
	
class Game(models.Model):
	title = models.CharField(max_length=255, unique=True)
	game_id = models.IntegerField()
	platforms = models.ManyToManyField(Platform)
	#release_date = models.DateField()
	overview = models.TextField(max_length=1000, blank=True)
	esrb = models.CharField(max_length=50, blank=True)
	#genres = models.ManyToManyField(Genre)
	players = models.IntegerField(default=1)
	co_op = models.BooleanField()
	publisher = models.CharField(max_length=255, blank=True)
	developer = models.CharField(max_length=255, blank=True)
	rating = models.DecimalField(max_digits=2, decimal_places=2)
	
	def __unicode__(self):
		return u'%s'%self.title