from django.db import models
from icheckgames.models import Game
from django.contrib.auth.models import User

# Create your models here.
class GameKeyword(models.Model):
        word = models.CharField(max_length=255, unique=True, db_index=True)
        title_games = models.ManyToManyField(Game, related_name='title_list')
        other_games = models.ManyToManyField(Game, related_name='other_list')
        
        def __unicode__(self):
                return u'%s'%self.word

class Recommendation(models.Model):
        user = models.ForeignKey(User, unique=True, db_index=True)
        gameslist = models.ManyToManyField(Game)
        
        def __unicode__(self):
                return u'%s'%self.user