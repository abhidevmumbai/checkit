from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save)
def userCreated(sender, instance, **kwargs):
    if sender.__name__ == "User":
        userprofile, created = UserProfile.objects.get_or_create(user=instance)


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.URLField(blank=True)
    cover = models.URLField(blank=True)
    facebookUser = models.BooleanField()
    facebookId = models.CharField(max_length=255, blank=True)
    facebookToken = models.TextField(blank=True)
    
    def __unicode__(self):
        return '%s'%self.user

class Platform(models.Model):
	name = models.CharField(max_length=255, unique=True, db_index=True)
	platform_id = models.IntegerField()
	alias = models.CharField(max_length=255, blank=True)
	overview = models.TextField(blank=True)
	developer = models.CharField(max_length=255, blank=True)
	manufacturer = models.CharField(max_length=255, blank=True)
	cpu = models.CharField(max_length=255, blank=True)
	memory = models.CharField(max_length=255, blank=True)
	graphics = models.CharField(max_length=255, blank=True)
	sound = models.CharField(max_length=255, blank=True)
	display = models.CharField(max_length=255, blank=True)
	media = models.CharField(max_length=255, blank=True)
	maxcontrollers = models.IntegerField(default=1)
	youtube_link = models.URLField(blank=True)
	rating = models.FloatField(default=0)
	boxarts = models.TextField(blank=True)
	fanarts = models.TextField(blank=True)
	banner = models.TextField(blank=True)
	
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
	overview = models.TextField(blank=True)
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
	status = models.CharField(max_length=255, db_index=True)
	owned = models.BooleanField(default=False)
	favorite = models.BooleanField(default=False)
	wish = models.BooleanField(default=False)
	
	def __unicode__(self):
		return u'%s'%self.game
	
	class Meta:
		unique_together = (("user", "game"),)
