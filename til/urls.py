from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from django.conf.urls import include
from mainapp import urls as mainapp_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(mainapp_urls, namespace="mainapp")),
    url('', include("allauth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
