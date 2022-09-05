from django.forms import ModelForm
from django import forms
from .models import *
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(UserCreationForm):
    class Meta:
         model = User
         fields = ['username', 'password1']
class UploadForm(ModelForm):
    class Meta:
         model = Upload
         exclude = ['owner','favourite']
class UploadSkripsiForm(ModelForm):
    class Meta:
         model = UploadSkripsi
         exclude = ['owner','favourite']
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({ 'class': 'form-control', 'type': 'email' })
        self.fields['alamat'].widget.attrs.update({ 'class': 'form-control', 'type': 'text' })
        self.fields['name'].widget.attrs.update({ 'class': 'form-control', 'type': 'text' })
        self.fields['profile_pic'].widget.attrs.update({ 'class': 'form-control', 'type': 'file' })

class EditProfileForm(ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    phone = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    alamat = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio','phone','alamat']