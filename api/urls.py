from django.urls import path, include


urlpatterns = [
    path("games/", include("api.games.urls")),
]
