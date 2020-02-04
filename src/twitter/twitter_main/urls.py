from django.contrib import admin
from django.urls import path
from . import views

app_name = 'twitter_main'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.user_register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('get_tweets/', views.get_tweets, name='get_tweets'),
    path('get_tweets/<int:amount>', views.get_tweets, name='get_tweets'),
    path('new_tweet/', views.post_tweet, name='post_tweet'),
]
