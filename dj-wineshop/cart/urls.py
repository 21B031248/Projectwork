from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^cart/$', cartApi),
    url(r'^cart_items/$', cartItemApi),
    url(r'^cart_item/([0-9]+)$', cartItemApi),
]
