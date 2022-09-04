from django.contrib import admin

from admin1.forms import UploadSkripsiForm
from .models import *
from admin1.models import Profile, UploadSkripsi,Upload

admin.site.register(UploadSkripsi)
admin.site.register(Upload)
# Register your models here.
