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
	
	def __unicode__(self):
		return u'%s'%self.name
	
class Game(models.Model):
	title = models.CharField(max_length=255)
	game_id = models.IntegerField()
	platform = models.ForeignKey(Platform)
	release_date = models.DateField(null=True, blank=True)
	overview = models.TextField(max_length=1000, blank=True)
	esrb = models.CharField(max_length=50, blank=True)
	genres = models.ManyToManyField(Genre)
	players = models.IntegerField(default=1)
	co_op = models.BooleanField()
	publisher = models.CharField(max_length=255, blank=True)
	developer = models.CharField(max_length=255, blank=True)
	rating = models.FloatField(default=0)
	youtube_link = models.URLField(blank=True)
	images = models.TextField(blank=True)
	
	def __unicode__(self):
		return u'%s'%self.title
	
	class Meta:
		unique_together = (("title", "platform"),)