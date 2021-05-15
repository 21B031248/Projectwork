from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wine.urls')),
    path('', include('checkout.urls')),
    path('', include('cart.urls'))
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
