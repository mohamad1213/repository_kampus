from django.forms import ModelForm
from .models import *
from home.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(UserCreationForm):
    class Meta:
         model = User
         fields = ['username', 'password1']

class ProfileUserForm2(ModelForm):
	class Meta:
		model = User
		fields = ['email']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['email'].widget.attrs.update({ 'class': 'form-control rounded border-secondary','type':'email', 'placeholder':'Email..','name':'email' })


class ProfileUserForm(ModelForm):
    class Meta:
        model = ProfileUser
        exclude = ['email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alamat'].widget.attrs.update({ 'class': 'form-control', 'type': 'text' })
        self.fields['name'].widget.attrs.update({ 'class': 'form-control', 'type': 'text' })
        self.fields['profile_pic'].widget.attrs.update({ 'class': 'form-control', 'type': 'file' })
        self.fields['phone'].widget.attrs.update({ 'class': 'form-control', 'type': 'number'})