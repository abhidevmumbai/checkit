from gamesearch.recommender import *
from django.contrib.auth.models import User

user = User.objects.all()[1]
recommender = Recommender()
recommender.build.apply_async([recommender, user], queue="recommender");
