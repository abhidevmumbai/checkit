from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Platform(models.Model):
	name = models.CharField(max_length=255, unique=True, db_index=True)
	platform_id = models.IntegerField()
	alias = models.CharField(max_length=255, blank=True)
	
	def __unicode__(self):
		return u'%s'%self.name

class Genre(models.Model):
	name = models.CharField(max_length=255, unique=True, db_index=True)
	
	def __unicode__(self):
		return u'%s'%self.name
	
class Game(models.Model):
	title = models.CharField(max_length=255, db_index=True)
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
	boxarts = models.TextField(blank=True)
	fanarts = models.TextField(blank=True)
	screenshots = models.TextField(blank=True)
	banner = models.TextField(blank=True)
	clearlogo = models.TextField(blank=True)
	
	def __unicode__(self):
		return u'%s'%self.title
	
	class Meta:
		unique_together = (("title", "platform"),)

class GameMap(models.Model):
	user = models.ForeignKey(User)
	game = models.ForeignKey(Game)
	owned = models.BooleanField(default=False)
	completed = models.BooleanField(default=False)
	current = models.BooleanField(default=False)
	onhold = models.BooleanField(default=False)
	favorite = models.BooleanField(default=False)
	wish = models.BooleanField(default=False)
	
	def __unicode__(self):
		return u'%s'%self.game
	
	class Meta:
		unique_together = (("user", "game"),)
