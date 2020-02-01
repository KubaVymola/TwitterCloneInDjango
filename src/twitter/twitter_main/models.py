from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=300)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

    
# class Tweet(models.Model):
#     tweet_text = models.CharField(max_length=280)