from django import forms
from .models import UserInfo, Tweet
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

class NewTweetForm(forms.ModelForm):
    # tweet_text = forms.CharField(max_length=280, widget=forms.TextInput )

    class Meta():
        model = Tweet
        fields = ( 'tweet_text', )