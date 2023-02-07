from django.urls import path

from .views import games

app_name = "games"


urlpatterns = [
    path("", games, name="games"),
    path("genre/<int:genre_id>", games, name="genre"),
    path("developers/<int:developer_id>", games, name="developer"),
]
