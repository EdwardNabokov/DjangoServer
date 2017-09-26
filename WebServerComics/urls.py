from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    url(r'^Comics/', include('Comics.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
