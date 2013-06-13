from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from captcha.fields import CaptchaField

class UsersForm(UserCreationForm):
    first_name = forms.CharField(max_length=255,required=True)
    last_name = forms.CharField(max_length=255,required=True)
    username = forms.EmailField(required=True)
    captcha = CaptchaField()
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    
    def save(self, commit=True):
        user = super(UsersForm, self).save(commit=False)
        user.email = self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class UsersEditForm(forms.Form):
    first_name = forms.CharField(max_length=255,required=True)
    last_name = forms.CharField(max_length=255,required=True)
    #email = forms.EmailField(required=True)
    old_password = forms.CharField()
    changepassword = forms.BooleanField(required=False)
    new_password1 = forms.CharField(required=False)
    new_password2 = forms.CharField(required=False)
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(UsersEditForm, self).__init__(*args, **kwargs)

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
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user