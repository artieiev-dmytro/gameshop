from django.urls import path

from .views import GamesListView

app_name = "games"


urlpatterns = [
    path("", GamesListView.as_view(), name="games"),
    path("genre/<int:genre_id>", GamesListView.as_view(), name="genre"),
    path("developers/<int:developer_id>", GamesListView.as_view(), name="developer"),
]
