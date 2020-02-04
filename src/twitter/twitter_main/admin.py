from django.contrib import admin
from .models import UserInfo, User, Tweet

admin.site.register(UserInfo)
admin.site.register(Tweet)