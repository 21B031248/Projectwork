from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^wines/$', wineApi),
    url(r'^wine/([0-9]+)$', wineApi, name='delete_wine')
]
