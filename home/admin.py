from django.contrib import admin

from admin1.forms import UploadSkripsiForm
from .models import *
from admin1.models import Profile, UploadSkripsi,Upload, Bookmark

admin.site.register(UploadSkripsi)
admin.site.register(Upload)
admin.site.register(Bookmark)
# Register your models here.
