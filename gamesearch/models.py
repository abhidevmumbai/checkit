from django.db import models
from icheckgames.models import Game

# Create your models here.
class GameKeyword(models.Model):
	word = models.CharField(max_length=255, unique=True, db_index=True)
	games = models.ManyToManyField(Game)
	
	def __unicode__(self):
		return u'%s'%self.word