from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from games.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("games/", include("games.urls", namespace="games")),
    path("users/", include("users.urls", namespace="users")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("accounts/", include("allauth.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
