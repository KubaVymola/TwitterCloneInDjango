from .forms import UserForm, UserInfoForm, NewTweetForm
from .models import UserInfo, Tweet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import json

@login_required
def index(request):
    tweet_form = NewTweetForm()

    return render(request, 'twitter_main/index.html', { 'tweet_form': tweet_form })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('twitter_main:index'))

def user_register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)
        
        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_info = user_info_form.save(commit=False)
            user_info.user = user
            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
            user_info.save()
            registered = True

    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    return render(request, 'twitter_main/register.html', { 'user_form': user_form, 'user_info_form': user_info_form, 'registered': registered } )



def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('twitter_main:index'))

    if request.method != 'POST': 
        return render(request, 'twitter_main/login.html', {})
    
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if not user:
        return HttpResponse('Invalid login credentials')

    if not user.is_active:
        return HttpResponse('Your account was inactive')
    
    login(request, user)


    request.session.set_expiry(0)
    if 'remember' in request.POST:
        request.session.set_expiry(60 * 60 * 24 * 30)

    if 'next' in request.GET:
        return HttpResponseRedirect(request.GET['next'])
    
    return HttpResponseRedirect(reverse('twitter_main:index'))


# @login_required
def get_tweets(request, amount=''):
    if not request.user.is_authenticated:
        return HttpResponseForbidden('You must be logged in to see the Tweets')

    if not amount:
        tweets = Tweet.objects.all().order_by('-pub_date')
    else:
        tweets = Tweet.objects.all().order_by('-pub_date')[:amount]

    return render(request, 'twitter_main/render_tweets.html', { 'tweets': tweets })


def post_tweet(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden('You must be logged in to post tweets')
    
    if request.method != 'POST':
        return HttpResponse('Use POST to Post tweet!')

    request_data = json.loads(request.body) #.decode('utf-8')
    new_tweet = Tweet(tweet_text=request_data['body'], author=request.user)
    new_tweet.save()

    return HttpResponse('Saved tweet')