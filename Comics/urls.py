from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # ex: /Comics/
    url(r'^$', views.index, name='index'),
    # ex: /Comics/5
    url(r'^(?P<image_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /Comcis/Savings
    url(r'^Savings/$', views.toSaveOriginal, name='saveImage'),

    url(r'^Color/$', views.toSaveColor, name='Color'),
]