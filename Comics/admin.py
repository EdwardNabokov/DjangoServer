from django.contrib import admin
from .models import UploadOriginal, UploadBlur


admin.site.register(UploadOriginal)
admin.site.register(UploadBlur)