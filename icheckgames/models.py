from django.db import models
from django.contrib.auth.models import User

# Create your models here.
''' Create User login table '''
class Gamers(models.Model):
	user = models.OneToOneField(User)

class Meta:
	verbose_name_plural = 'Gamers'

def __unicode__(self):
	return self.user.username