from django.urls import path

from .views import GamesListView, GameDetailView, rating, create_comment, SearchView

app_name = "games"


urlpatterns = [
    path("", GamesListView.as_view(), name="games"),
    path("<slug:slug>", GameDetailView.as_view(), name="game_detail"),
    path("comment/<int:game_id>", create_comment, name="create_comment"),
    path("genre/<slug:slug_genre>", GamesListView.as_view(), name="genre"),
    path("developers/<slug:slug_developer>", GamesListView.as_view(), name="developer"),
    path("rating/<int:game_id>", rating, name="rating"),
    path("search/", SearchView.as_view(), name="search"),
]
