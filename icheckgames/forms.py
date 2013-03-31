from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from models import Users
from captcha.fields import CaptchaField

class UsersForm(UserCreationForm):
    first_name = forms.CharField(max_length=255,required=True)
    last_name = forms.CharField(max_length=255,required=True)
    #email = forms.EmailField(required=True)
    username = forms.EmailField(required=True)
    organization = forms.CharField(max_length=255)
    website = forms.URLField(required=False)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    
    def save(self, commit=True):
        print "In save function"
        user = super(UsersForm, self).save(commit=False)
        user.email = self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            new_developer = Developers(user=user)
            new_developer.generate_secret_key()
            new_developer.generate_developer_key()
            new_developer.organization = self.cleaned_data["organization"]
            new_developer.website = self.cleaned_data["website"]
            new_developer.save()
        return user