from django.contrib import admin
from django.urls import path, include

from games.views import index

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("games/", include(("games.urls", "games"))),
]
