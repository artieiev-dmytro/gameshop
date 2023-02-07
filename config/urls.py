from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from games.views import index

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("games/", include("games.urls", namespace="games")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
