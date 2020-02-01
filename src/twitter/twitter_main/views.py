from .forms import UserForm, UserInfoForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'twitter_main/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, user {}".format(request.user.UserInfo.about))

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

    if 'next' in request.GET:
        return HttpResponseRedirect(request.GET['next'])
    
    return HttpResponseRedirect(reverse('twitter_main:index'))
