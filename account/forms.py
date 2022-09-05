from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import utils
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({ 'class': 'form-control rounded','type': 'text','placeholder':'Nama Pengguna..' })
		self.fields['email'].widget.attrs.update({ 'class': 'form-control rounded','type':'email', 'placeholder':'Email..' })
		self.fields['password1'].widget.attrs.update({ 'class': 'form-control rounded', 'type':'password' , 'placeholder':'Password..' })
		self.fields['password2'].widget.attrs.update({ 'class': 'form-control rounded','type':'password' , 'placeholder':'Re-Password..' })

class PasswordResetForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({ 'class': 'form-control rounded','type': 'text','placeholder':'Nama Pengguna..' })
	def get_password_reset_url(self):
		base64_encoded_id = utils.http.urlsafe_base64_encode(utils.encoding.force_bytes(self.id))
		token = PasswordResetTokenGenerator().make_token(self)
		reset_url_args = {'uidb64': base64_encoded_id, 'token': token}
		reset_path = reverse('reset_passsword', kwargs=reset_url_args)
		reset_url = f'{settings.BASE_URL}{reset_path}'
		return reset_url