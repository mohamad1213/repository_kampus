from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({ 'class': 'form-control','type': 'text','placeholder':'username..' })
		self.fields['email'].widget.attrs.update({ 'class': 'form-control','type':'email', 'placeholder':'Email..' })
		self.fields['password1'].widget.attrs.update({ 'class': 'form-control', 'type':'password' , 'placeholder':'Password..' })
		self.fields['password2'].widget.attrs.update({ 'class': 'form-control','type':'password' , 'placeholder':'Re-Password..' })
