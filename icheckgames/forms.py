from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from models import Gamers
from captcha.fields import CaptchaField

class GamersForm(UserCreationForm):
    first_name = forms.CharField(max_length=255,required=True)
    last_name = forms.CharField(max_length=255,required=True)
    username = forms.EmailField(required=True)
    

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    
    def save(self, commit=True):
        print "In save function"
        user = super(GamersForm, self).save(commit=False)
        user.email = self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            new_user = Gamers(user=user)
            new_user.save()
        return user