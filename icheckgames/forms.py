from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from captcha.fields import CaptchaField

class UsersForm(UserCreationForm):
    first_name = forms.CharField(max_length=255,required=True)
    last_name = forms.CharField(max_length=255,required=True)
    username = forms.CharField(max_length=30,required=True)
    email = forms.EmailField(required=True)
    captcha = CaptchaField()
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    
    def save(self, commit=True):
        user = super(UsersForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
        return user

class UsersEditForm(forms.Form):
    cover = forms.URLField(required=False)
    avatar = forms.URLField(required=False)
    first_name = forms.CharField(max_length=255,required=True)
    last_name = forms.CharField(max_length=255,required=True)
    username = forms.CharField(max_length=255,required=True)
    #email = forms.EmailField(required=True)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(UsersEditForm, self).__init__(*args, **kwargs)
        if not user.userprofile.facebookUser:
            self.fields['old_password'] = forms.CharField()
            self.fields['new_password1'] = forms.CharField(required=False)
            self.fields['new_password2'] = forms.CharField(required=False)
            self.fields['changepassword'] = forms.BooleanField(required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username "%s" is already in use.' % username)
        return username

    def clean_new_password2(self):
        password1 = self.cleaned_data['new_password1']
        password2 = self.cleaned_data['new_password2']
        if self.cleaned_data.get('changepassword'):
            if password1 and password2:
                if password1 != password2:
                    raise forms.ValidationError("The two password fields didn't match.")
            else:
                raise forms.ValidationError("New passwords are required.")
        return password2

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError("Your old password was entered incorrectly. Please enter it again.")
        return old_password

    def save(self, commit=True):
        user = self.user
        if self.cleaned_data.get('changepassword'):
            user.set_password(self.cleaned_data['new_password1'])
        #user.email = self.cleaned_data["email"]
        user.userprofile.cover = self.cleaned_data['cover']
        user.userprofile.avatar = self.cleaned_data['avatar']
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["username"]
        
        if commit:
            user.save()
            user.userprofile.save()
        return user