from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class FacebookBackend(ModelBackend):
    
    def authenticate(self, username):
        try:
            user = User.objects.get(username=username)
            if user.userprofile.facebookUser:
                return user
        except User.DoesNotExist:
            return None