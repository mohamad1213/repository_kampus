from django.contrib import admin

from admin1.forms import UploadSkripsiForm
from .models import *
from admin1.models import UploadSkripsi,Upload, Bookmark

admin.site.register(UploadSkripsi)
admin.site.register(Upload)
admin.site.register(Bookmark)
admin.site.register(ProfileUser)
# Register your models here.
