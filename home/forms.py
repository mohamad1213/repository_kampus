from django.forms import ModelForm
from .models import *
from home.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(UserCreationForm):
    class Meta:
         model = User
         fields = ['username', 'password1']

class ImageForm(ModelForm):
    class Meta:
         model = Home
         fields = ['logo']
    