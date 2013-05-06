from django.db import models
from django.contrib.auth.models import User

# Create your models here.
''' Create User login table '''
class Users(models.Model):
	user = models.OneToOneField(User)

class Meta:
	verbose_name_plural = 'Users'

def __unicode__(self):
	return self.user.username