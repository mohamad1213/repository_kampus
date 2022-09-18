
from django.db import models
from admin1.models import *
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    alamat = models.TextField(null=True)
    profile_pic = models.ImageField(upload_to="profile",default='defaultavatar.png',null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.name) if self.name else ''
