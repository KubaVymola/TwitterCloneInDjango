from django import forms
from .models import UserInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ( 'username', 'password', 'email' )

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ( 'about', 'profile_pic' )